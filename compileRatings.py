import pickle
import os
import json
import string
import nltk
import configparser
import re
import jsonToHTML

# takes layup JSON reviews and outputs courses / professors
# with predictions

#################################################
# LOAD TRAINED MODEL
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
     
filename_model = 'classifier.pkl'
classifier = pickle.load(open(filename_model, 'rb'))
filename_vec = 'vectorizor.pkl'
vectorizor = pickle.load(open(filename_vec, 'rb'))

#################################################
# ALGORITHM
# load json object
reviews = json.load(open('layup_reviews.json'))
# sort by course codes (append department attribute with number)
def get_course_code(json):
    return json["department"] + json["number"]
reviews.sort(key=get_course_code)

# filter out empty comments
def filter_pred(json):
    return len(json["comments"]) > 0
reviews = filter(filter_pred, reviews)
print(reviews)


# sorts each course's sublist by professor's name
def get_professor(json):
    return json["professor"]
sectioned_reviews = []
temp_section = []
prev = ""
for review in reviews:
    if get_course_code(review) == prev or prev == "":
        temp_section.append(review)
    else:
        temp_section.sort(key=get_professor)
        sectioned_reviews += temp_section
        temp_section = [review]
    prev = get_course_code(review)

# iterate through sectioned_reviews, model-predict each comment (course / professor if applicable)
# and construct json object by averaging the same professor's ratings'
output = []
temp_sum = 0
counter = 1
prev_prof = ""
prev_course = ""
for review in sectioned_reviews:
    full_review = ""
    if "course" in review["comments"]:
        full_review += review["comments"]["course"]
    if "professor" in review["comments"]:
        full_review += " " + review["comments"]["professor"]
    if "workload" in review["comments"]:
        full_review += " " + review["comments"]["workload"]
    features = vectorizor.transform([full_review])
    rating = classifier.predict(features)
    if review["professor"] == prev_prof or prev_prof == "":
        temp_sum += rating
        counter += 1
    else:
        average_rating = temp_sum / counter
        output.append({"course": prev_course,
                       "professor": prev_prof,
                       "rating": str(average_rating)})
        temp_sum = rating
        counter = 1
    prev_prof = review["professor"]
    prev_course = get_course_code(review)



with open('parsed.json', 'w') as outfile:
    json.dump(output, outfile)
print("Done.")