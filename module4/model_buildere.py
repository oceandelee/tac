"""Iterate over sentences to build word2vec model"""
import os
import logging
import sys

from gensim.models.phrases import Phrases, Phraser
from gensim.models import Word2Vec

import nltk
from nltk.tokenize import wordpunct_tokenize

nltk.data.path.append(r"C:\Users\admin\AppData\Local\Programs\Python\Python37")

logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences(object):
    """Tokenize and Lemmatize sentences"""
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        for line in open(self.filename, encoding='utf-8', errors="backslashreplace"):
            yield [w.lower() for w in wordpunct_tokenize(line)]
currentpath= os.path.dirname(os.path.abspath(__file__))
infile =  currentpath +fr"\data\sents.txt"
sentences = MySentences(infile)
print("phrase1")
phrases = Phrases(sentences)
print("phraser")
bigram = Phraser(phrases)
print("phrase2")
trigram = Phrases(bigram[sentences])
print("list")
corpus = trigram[bigram[sentences]] #list(trigram[bigram[sentences]])
print("model")
model = Word2Vec(corpus, size=32, window=5, min_count=5, workers=2, iter=2)
print("end")
outfile = currentpath +fr"\data\bulletins.model"
model.save(outfile)
