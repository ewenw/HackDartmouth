import nltk

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