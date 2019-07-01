# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 07:59:02 2019

@author: translucky
"""

import time

book_words=file_handle=open('alice_in_wonderland.txt',mode='r')
#("alice_in_wonderland.txt")
bigger_vocab=file_handle=open('vocab.txt',mode='r')

def search_linear(xs, target):
    for (i, v) in enumerate(xs):
       if v == target:
           return i
    return -1

def find_unknown_words(vocab, wds):
    result = []
    for w in wds:
        if (search_linear(vocab, w) < 0):
            result.append(w)
    return result

t0 = time.clock()
missing_words = find_unknown_words(bigger_vocab, book_words)
t1 = time.clock()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))
 
