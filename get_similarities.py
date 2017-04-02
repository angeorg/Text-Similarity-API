#!/usr/bin/python

import sys
from gensim import corpora, models, similarities

resource_id = sys.argv[1]
sentence = sys.argv[2]

dict_name = '/tmp/' + resource_id + '.dict'
corpus_name = '/tmp/' + resource_id + '.mm'
index_name = '/tmp/' + resource_id + '.index'

dictionary = corpora.Dictionary.load(dict_name)
corpus = corpora.MmCorpus(corpus_name)

lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

vec_bow = dictionary.doc2bow(sentence.lower().split())
vec_lsi = lsi[vec_bow]

index = similarities.MatrixSimilarity(lsi[corpus])
index.save(index_name)
index = similarities.MatrixSimilarity.load(index_name)

sims = index[vec_lsi]

print list(sims)
