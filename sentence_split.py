


def sentence_split(file_name):
    #file = open(file_name, "r")
    #filedata = file_name.read()
    filedata = file_name.split(".")
    sentences = []

    for sentence in filedata:
        sentence = sentence.replace("[^a-zA-Z]", " ")
        sentence = sentence.replace('\n', " ")
        sentence = sentence.replace("  "," ")
        sentence = sentence.replace("[^A-Za-z0-9]+"," ")
        sentence = sentence.replace('"'," ")
        #only removing single quotes otherwise will lost apostrophes.
        #These should be removed in tokenization anyway.
        sentence = sentence.replace(','," ")
        sentence = sentence.strip()


        sentences.append(sentence)

    return sentences
