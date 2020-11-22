"""Playing with word2vec model"""

#%%
import os
from gensim.models import Word2Vec
from pprint import pprint

currentpath= os.path.dirname(os.path.abspath(__file__))

model = Word2Vec.load(currentpath + fr"\data\bulletins.model")

word1 = "egout"
pprint(model.wv[word1])

#%%
word2 = "eau"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

#%%
word2 = "travaux"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

#%%
pprint(model.wv.most_similar("moyen", topn=3))

#%%
pprint(model.wv.most_similar("revenus"))

#%%
pprint(model.wv.most_similar(positive=['chantier', 'ouvrier'], negative=['cout']))
