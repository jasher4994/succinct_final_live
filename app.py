#package import
import sys
from flask import Flask, render_template, request,redirect, url_for, send_from_directory
from sentence_split import sentence_split
from sentiment import analyze_sentiment, pace, readability
from sentiment import moving_average
import openai

secret_key = "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"
openai.api_key = secret_key

app = Flask(__name__)

@app.route('/ads.txt')
def ads():
    return send_from_directory(app.static_folder, 'ads.txt')



def emotion_scale(x):
    if int(x) < 2:
        return 'keep the level of emotion the same'
    elif int(x) < 5:
        return 'increase the emotion of the language moderately'
    elif int(x) < 8:
        return 'increase the emotion of the language significantly'
    else:
        return 'increase the emotion of the langage as much as possible'

def formality_scale(x):
    if int(x) < 2:
        return 'keep the formality of the language the same'
    elif int(x) < 5:
        return 'increase the formality of the language moderately'
    elif int(x) < 8:
        return 'increase the formality of the language significantly'
    else:
        return 'increase the formality of the language as much as possible'


def summarise_scale(x):
    if int(x) < 3:
        return 'dont shorten the text at all'
    elif int(x) < 5:
        return 'shorten the text by 20%'
    elif int(x) < 8:
        return 'shorten the text by 50%'
    else:
        return 'summarize the text as much as possible'

@app.route("/")
def home():
    with app.open_resource('static/books/The Hunger Games.txt') as f:
        text = f.read()
        text = str(text)
        text = sentence_split(text)

        sentiment_scores = analyze_sentiment(text)
        sentiment_scores = list(moving_average(sentiment_scores))
    return render_template('home.html', data = sentiment_scores, text = text )

@app.route("/test")
def test():
    return render_template('test.html')

@app.route("/book", methods = ['GET', 'POST'])
def book():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            text = uploaded_file.read()
            text = str(text)
            text = sentence_split(text)

            sentiment_scores = analyze_sentiment(text)
            sentiment_scores = list(moving_average(sentiment_scores))

            pace_scores = pace(text)
            pace_scores = list(moving_average(pace_scores))
            pace_scores = [x-0.5 for x in pace_scores]

            readability_scores = readability(text)
            readability_scores = list(moving_average(readability_scores))
            readability_scores = [x-0.5 for x in readability_scores]

            return render_template('book_output.html', sentiment_data = sentiment_scores, pace_data = pace_scores, readabilty_data = readability_scores, text = text, filename = uploaded_file.filename)
    return render_template('book.html')

@app.route("/page")
def page():
    return render_template('page.html')

@app.route("/about")
def about():
    return render_template('about.html')
"""
@app.route("/edit", methods=("GET", "POST"))
def edit():
    if request.method == "POST":
        text = request.form["text"]
        if request.form["emotion"] == '1' and request.form["formality"] == '1' and request.form["summarise"] == '1':
            result = text
        else:
            emotion = emotion_scale(request.form["emotion"])
            formality = formality_scale(request.form["formality"])
            summarise = summarise_scale(request.form["summarise"])
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=generate_prompt(emotion, formality, summarise,text),
                temperature=0.9,
                max_tokens=1000
            )
            result=response.choices[0].text

        return redirect(url_for("edit", result = result ))

    result = request.args.get("result")
    return render_template("edit.html", result=result)

"""
def generate_prompt(emotion, formality, summarise, text):
    return """Take the text in the next sentence and {}, and {}, and {}. Here is the text: {} """.format(emotion, formality, summarise, text)


@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = '404'), 404




if __name__ == "__main__":
    #freezer.freeze creates a static site. len(sys.argv checks whether any additional arguments have been passed to the script when running.)
    #sys.argv[1] captures the first argument, sys.argv[0] is always the script name.
    #Therefore, running 'python app.py build' will trigger freezer.freeze and create a static directory called build.
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        #running normally. remove debug=True when hosting properly.
        app.run()


