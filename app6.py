# stemming, troncatura di parole derivate alla root
# uno dei piu comuni algoritmi di stemming è il PORTERSTEMMER

from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
pstem= PorterStemmer() # create un'istanza della classe PorterStemmer

print(pstem.stem('presumably'))

#ORA IMPORTO UN ATLRO STEMMER DETTO LANCASTER STEMMER
lstem= LancasterStemmer()
#molto + aggressivo
print(lstem.stem('presumably'))

# Si puo usare anche il nostro stemmer custom usando RegexpStemmer
# from nltk.stem import RegexpStemmer

