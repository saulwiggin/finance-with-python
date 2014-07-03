"""
  Name     : 4375OS_10_29_generate_bible_unique_words.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
  location : http://pentecostalsofdadeville.com/documents/AV1611Bible.txt
  http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.to_pickle.html#pandas.DataFrame.to_pickle
  
"""

from string import maketrans
import pandas as pd
word_freq = {}
word_list = open("c:/temp/AV1611Bible.txt", "r").read().split()
for word in word_list:
    word = word.translate(maketrans("",""), '!"#$%&()*+,./:;<=>?@[\\]^_`{|}~0123456789')
    if word.startswith('-'): word = word.replace('-','')
    if len(word): word_freq[word] = word_freq.get(word, 0) + 1
keys = sorted(word_freq.keys())
x=pd.DataFrame(keys)
x.to_pickle('c:/temp/uniqueWords.pickle')

    