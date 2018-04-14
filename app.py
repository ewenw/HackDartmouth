from flask import Flask, render_template, json, request
app = Flask(__name__)

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

     if _comment:
     	return json.dumps({'html':'All fields good!'})
     else:
     	return json.dumps({'html':'enter the required fields'})

if __name__ == "__main__":
    app.run()