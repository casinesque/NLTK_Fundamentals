#FREQUENCY DISTRIBUTION IN NLTK

from nltk import ConditionalFreqDist, FreqDist
s = 'She shines and she signs she sits instead of typing it'
#Prima cosa la tokenizziamo
list = s.split()
print(list)
# Ne calcoliamo la frequency distribution
fd = FreqDist(list)
print(fd)
#mostra i due termini piu frequenti
print(fd.most_common(2))
