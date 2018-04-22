from flask import Flask, render_template, json, request
import pickle
import os
import json
import string
import nltk
import configparser
import re
import json_to_html
import sys

#import pandas as pd

def stem_tokens(tokens):
    stemmed = []
    for item in tokens:
        stemmed.append(item)
        #stemmed.append(stemmer.stem(lemmatizer.lemmatize(item)))
        #stemmed.append(lemmatizer.lemmatize(item))
    return stemmed

def tokenize(paragraph):
    tokens = []
    for sentence in nltk.sent_tokenize(paragraph):
        for word in nltk.word_tokenize(sentence):
            tokens.append(word)
    stems = stem_tokens(tokens)
    return stems

app = Flask(__name__)


     


# conn = mysql.connect()

# cursor = conn.cursor()

# basic route
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/layup',methods=['GET'])
def layup():
     raw = json.load(open('parsed.json'))
     for msg in raw:
        msg["rating"] = msg["rating"].replace("[", "").replace("]","")
 
     return render_template("results.html", post=raw)


@app.route('/signUp',methods=['POST'])
def signUp():
    with open('classifier.pkl', 'rb') as f:
        classifier = pickle.load(f)
    with open('vectorizor.pkl', 'rb') as f:
        vectorizor = pickle.load(f)

    _comment = request.form['inputComment']
    features = vectorizor.transform([_comment])
    predicted_rating = classifier.predict(features)
    
    raw={"rating":str(predicted_rating[0])}
    print(str(raw), file=sys.stdout)
    sys.stdout.flush()
    return render_template("rate_result.html", post=raw)
    
app.run()
