#CONDITIONAL FREQUENCY DISTRIBUTION

from nltk import ConditionalFreqDist, FreqDist
from nltk.corpus import brown
l1= [('cat1','good'),('cat2','bad'),('cat1','good')]
cfd = ConditionalFreqDist(l1)
print(cfd.items())

#calcola una frequenza condizionata, quindi la frequenza di ogni parola a seconda delle due dimensioni di riferimento
#che scegliamo
cfd = ConditionalFreqDist(
    (genre,word)
    for genere in brown.categories()
    for word in brown.words(categories=genre))
genres=['news','religion','hobbies','science_fiction','romance','humor']
modals=['can','could','may','might','must','will']

