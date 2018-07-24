from nltk.corpus import PlaintextCorpusReader


# Link to download plays in txt format of Shakespeare - http://www.textfiles.com/etext/AUTHORS/SHAKESPEARE/

import os

corpus_root = os.getcwd() + '/'
file_ids = '.*.txt'
wordlists = PlaintextCorpusReader(corpus_root, file_ids)
print(wordlists.fileids())
print(wordlists.words('shakespeare-taming-of-the-shrew.txt'))