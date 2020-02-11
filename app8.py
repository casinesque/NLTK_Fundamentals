# TOKENIZATION
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import  gutenberg
print(gutenberg.fileids())
r = gutenberg.raw('austen-emma.txt')
print(r)
emma = r[50:477]
print(emma)
s = sent_tokenize(emma)  # crea una lista di due sentences. Equivale ad uno split('.')
print(s)
w = word_tokenize(emma)
print(w)