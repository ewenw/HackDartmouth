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

app = Flask(__name__)


class Tokenizer():
    def stem_tokens(self, tokens):
        stemmed = []
        for item in tokens:
            stemmed.append(item)
            #stemmed.append(stemmer.stem(lemmatizer.lemmatize(item)))
            #stemmed.append(lemmatizer.lemmatize(item))
        return stemmed

    def tokenize(self, paragraph):
        tokens = []
        for sentence in nltk.sent_tokenize(paragraph):
            for word in nltk.word_tokenize(sentence):
                tokens.append(word)
        stems = self.stem_tokens(tokens)
        return stems
    
tokenizer = Tokenizer()
     

filename_model = 'classifier.pkl'
classifier = pickle.load(open(filename_model, 'rb'))
filename_vec = 'vectorizor.pkl'
vectorizor = pickle.load(open(filename_vec, 'rb'))

# conn = mysql.connect()

# cursor = conn.cursor()

# basic route
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/layup',methods=['GET'])
def layup():
     raw = json.load(open('parsed.json'))
     for msg in raw:
        msg["rating"] = msg["rating"].replace("[", "").replace("]","")
 
     return render_template("results.html", post=raw)


@app.route('/signUp',methods=['POST'])
def signUp():
     _comment = request.form['inputComment']
     features = vectorizor.transform([_comment])
     predicted_rating = classifier.predict(features)
     
     raw={"rating":str(predicted_rating[0])}
     print(str(raw), file=sys.stdout)
     sys.stdout.flush()
     return render_template("rate_result.html", post=raw)
    
app.run()
