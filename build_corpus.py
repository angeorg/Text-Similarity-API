#!/usr/bin/python

import sys
from gensim import corpora

resource_id = sys.argv[1]
data = [x.strip() for x in  sys.argv[2].split(',')]

dict_name = '/tmp/' + resource_id + '.dict'
corpus_name = '/tmp/' + resource_id + '.mm'

# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in data]

# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
         for text in texts]

dictionary = corpora.Dictionary(texts)
dictionary.save(dict_name)  # store the dictionary, for future reference
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize(corpus_name, corpus)  # store to disk, for later use
