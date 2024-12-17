import gensim
word2vec = gensim.models.KeyedVectors.load_word2vec_format(
    "cbow.txt", binary=False
)

pos = ["проблема_NOUN"]
neg = ["позабывать_VERB"]

# pos = ["проблема_NOUN"]
# neg = ["ах_INTJ"]

dist = word2vec.most_similar(
    positive=pos,
    negative=neg
)

for i in dist:
  print(i)