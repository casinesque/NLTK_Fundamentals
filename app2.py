from nltk.corpus import brown
print(brown.categories()) #brown è un corpus suddiviso per categorie
#supponendo che voglia accedere solamente a quelli di humour
print(brown.fileids(categories=['humor']))
print(brown.raw('cr01'))
# corpusname.fileids() --> restituisce la lista dei file nel corpus
# con brown e altri è possibile cercare le parole o le sentences per categoria!
#print(brown.words(categories=list_of_categories))
#print(brown.sents(categories=list_of_categories))
print(brown.root)

