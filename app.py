from flask import Flask, render_template, json, request
import mysql.connector
from flaskext.mysql import MySQL
#import pickleimport 
#import os
##import json
##import string
#import nltk
#import pandas as pd

app = Flask(__name__)

# mysql = MySQL()

# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
# app.config['MYSQL_DATABASE_DB'] = 'HackDartmouth'
'''app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)'''

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='HackDartmouth')

#filename_model = 'model.pkl'
#loaded_model = pickle.load(open(filename_model, 'rb'))
#filename_vec = 'vectorizor.pkl'
#vectorizor = pickle.load(open(filename_vec, 'rb'))

# conn = mysql.connect()

# cursor = conn.cursor()

# basic route
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/contact')
def contact():
     return render_template('contact.html')

@app.route('/signUp',methods=['POST'])
def signUp():
     _comment = request.form['inputComment']

     # parse comment 

     predicted_rating = 5

     # features = vect.transform([_comment])
     # predicted_rating = loaded_model.predict(features)

     cursor1 = cnx.cursor()

     sqltext = "INSERT INTO HackDartmouth.comments (comment, rating) VALUES ('"+_comment+"', "+ str(predicted_rating) +")"

     result = cursor1.execute(sqltext)

     cnx.commit()

     cnx.close()

     # data = cursor.fetchall()

     if _comment:
        return json.dumps({'html':result})
     else:
        return json.dumps({'html':'enter the required fields'})



if __name__ == "__main__":
    app.run()
