import nltk
from nltk.corpus import  gutenberg
#print(gutenberg.fileids())
bibler=gutenberg.raw('bible-kjv.txt') #raw method stampa tutto il testo come un' unica stringa di caratteri
print(bibler[4153])
#word method, stampa la bibbia suddivia per words
biblew=gutenberg.words('bible-kjv.txt')
print(type(biblew))
print(biblew[:100])
# accessing corpus in sentences
bibles=gutenberg.sents('bible-kjv.txt')
print(bibles) #ogni sentences è una lista di parola al suo interno!