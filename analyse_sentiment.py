# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 16:49:56 2023

@author: James Asher
"""

from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from scipy.ndimage.filters import gaussian_filter1d
import pandas as pd
from scipy.signal import savgol_filter

def sentence_split(file_name):
    with open(file_name, mode = 'r',encoding="utf8") as f:
        data = f.read()
    
    filedata = data.split(".")
    sentences = []

    for sentence in filedata:
        sentence = sentence.replace("[^a-zA-Z]", " ")
        sentence = sentence.replace('^\n', " ")
        sentence = sentence.replace('^\r', " ")
        sentence = sentence.replace("  "," ")
        sentence = sentence.replace("[^A-Za-z0-9]+"," ")
        sentence = sentence.replace('"'," ") 
        #only removing single quotes otherwise will lose apostrophes. 
        #These should be removed in tokenization anyway. 
        sentence = sentence.replace(','," ")
        sentence = sentence.strip()


        sentences.append(sentence)
 
    return sentences

def analyze_sentiment(sentences):
    analyzer = SentimentIntensityAnalyzer()
    sentence_scores = []
    for sentence in sentences:
        vs = analyzer.polarity_scores(sentence)
        sentence_scores.append(vs['compound'])
        
    return sentence_scores

def moving_average(sentence_scores, polyorder = 1, window_length = 10):
    
    window = round(len(sentence_scores)/window_length)
    if (window % 2) == 0:
        window += 1
    if window <= 3:
        window = 3
    mov_avg_normalised = savgol_filter(sentence_scores, window, polyorder, mode = 'mirror')
    trim = round(len(sentence_scores)/(window_length/2))
    mov_avg_normalised = mov_avg_normalised[trim:]

    return mov_avg_normalised