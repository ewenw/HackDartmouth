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
import tokenizer
from tokenizer import Tokenizer
import logging

#import pandas as pd

app = Flask(__name__, template_folder='templates')

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

filename_model = 'classifier.pkl'
classifier = pickle.load(open(filename_model, 'rb'))

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
    tokenizer = Tokenizer()
    filename_vec = 'vectorizor.pkl'
    vectorizor = pickle.load(open(filename_vec, 'rb'))
    _comment = request.form['inputComment']
    features = vectorizor.transform([_comment])
    predicted_rating = classifier.predict(features)

    raw={"rating":str(predicted_rating[0])}
    print(str(raw), file=sys.stdout)
    sys.stdout.flush()
    return render_template("rate_result.html", post=raw)
if __name__ == '__main__':
    app.run()
