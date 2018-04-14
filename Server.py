from flask import Flask, render_template, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
app = Flask(__name__)

class ContactForm(Form):
  name = TextField("Name",  [validators.Required()])
  comment = TextAreaField("Comment",  [validators.Required()])
  submit = SubmitField("Send")


@app.route('/form', methods=['GET', 'POST'])
def form():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('form.html', form=form)
    else:
      return 'Form posted.'
 
  elif request.method == 'GET':
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run()