from sentence_split import sentence_split
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from scipy.signal import savgol_filter
import textstat



def analyze_sentiment(sentences):
    analyzer = SentimentIntensityAnalyzer()
    sentence_scores = []
    for sentence in sentences:
        vs = analyzer.polarity_scores(sentence)
        sentence_scores.append(vs['compound'])

    return sentence_scores

def pace(sentences):
    pace_scores = []
    for sentence in sentences:
        pace_scores.append(len(sentence))
    norm = [float(i)/max(pace_scores) for i in pace_scores]
    return norm


def readability(sentences):

    readability_scores = []
    for sentence in sentences:
        readability_scores.append(textstat.flesch_reading_ease(sentence))
    norm = [float(i)/max(readability_scores) for i in readability_scores]
    return norm






def moving_average(sentence_scores, polyorder = 1, window_length = 10):

    window = round(len(sentence_scores)/window_length)
    if (window % 2) == 0:
        window += 1
    if window <= 3:
        window = 3
    mov_avg_normalised = savgol_filter(sentence_scores, window, polyorder, mode = 'mirror')
    #trim = round(len(sentence_scores)/(window_length/2))
    #mov_avg_normalised = mov_avg_normalised[trim:]

    return mov_avg_normalised