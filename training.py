
# coding: utf-8

# In[25]:


import os
import json
import string
import nltk
import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import numpy as np
from sklearn import metrics
from sklearn.metrics import pairwise_distances
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn import linear_model
from sklearn.externals import joblib
    
wordnet_lemmatizer = WordNetLemmatizer()


with open('yelp.json') as data_file:    
    yelp = json.load(data_file)
#with open('yelp.json') as data_file:    
    #yelp = json.load(data_file)


# In[26]:



#nltk.download('punkt')
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

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

scores = []
corpora = []
for review in yelp:
    for category in review:
        if "text" in category:
            corpora.append(review[category])
        elif "stars" in category:
            scores.append(review[category])

vect = TfidfVectorizer(tokenizer=tokenize)
matrix = vect.fit_transform(corpora)

test = vect.transform(["decent"])
#vect.get_feature_names()


# In[27]:


clf = linear_model.SGDClassifier()
clf.fit(matrix, np.array(scores)) 
with open('classifier.pkl', 'wb') as output:
    pickle.dump(clf, output, protocol=2)
with open('vectorizor.pkl', 'wb') as output:
    pickle.dump(vect, output, protocol=2)


# In[28]:



#for i in range(100):
    #print(clf.predict(matrix[i]))
print(clf.predict(test[0]))


# In[18]:




