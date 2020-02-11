from nltk.corpus import brown
from nltk import FreqDist
l_w_humor=brown.words(categories='humor')
#print(l_w_humor)
#restituisco i docs di caterogira humor suddiviso in parole (words)
#vediamo di ritornare la frequenza delle parole in questo tipo di testo
fd_w_humor=FreqDist(l_w_humor)
print(fd_w_humor.most_common(10))
#troppe stopwwords, non abbiamo idea di nessun topic per questo testo
#HAPAXES, TERMINI CHE APPAIONO UNA SOLA VOLTA
print(fd_w_humor.hapaxes())
#MAX, RESTITUISCE SEMPLICEMENTE LA MOST FREQUENT WORD. SARA' SEMPRE IL PRIMO ELEMENTO DEI MOST COMMONS

print(fd_w_humor.max())

#freq function, esegue il term frequency TF. Ovvero è il rapporto tra il numero delle occorrenze di quel termine
# e il numero totale di parole in quel testo ----- TF = tf/wn

freq_the=fd_w_humor.freq('the')
print(freq_the)

## si vuole la riprova? --> si fa fd_w_humor.get('the)/length of the text