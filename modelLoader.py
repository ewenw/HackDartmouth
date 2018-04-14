
import pickle

filename = 'model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


# new post: parse, predict, send back to user, store original text + score into SQL
result = loaded_model.predict(features)
def signUp():
     comment = request.form['inputComment']
     features = parse(comment)
