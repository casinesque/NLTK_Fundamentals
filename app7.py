#LEMMATIZATION, cerca di ricondurci alla root di una parola simile ma basandosi sul significato della parola e non sulla sua sintassi come fa Stemming

#Si usa WordNet corpus dove le parole sono mappate a seconda dei loro significati. Praticamente
#Wordnet contiene un bacino di sinonimi, antonyms, hyponyms, hypernyms

from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
print(wn.synsets('spoke')) #vediamo che restiutisce alcune parole con alcune statistiche accanto
print(wn.synset('talk.v.01').definition()) # restituisce la definizione di una delle parole ritornate
wn.synset('talk.v.01').examples() # restituisce alcuni esempi della parola e contesti di utilizzo
wnl = WordNetLemmatizer()
wnl.lemmatize('spoken','v') # --> passo il 2 parametro come contesto quindi v è per dire verbo. Di default è a noun.
wnl.lemmatize('worst','a') # --> qui resttuisce bad. Con 'a' passo un contesto di aggettivo




