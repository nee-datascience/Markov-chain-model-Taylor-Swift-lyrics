# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 16:18:54 2020

@author: Nee Data Science
"""

# Import required package
import numpy as np

# Load set from input file
input = open('D:/python/lyrics/taylor_swift/myfav2.txt', encoding='utf8').read()
#print(input)

# Split data into words
words = input.split()
#print(words)

# Define function to create pairs to keys
def pairs_keys(words):
    for i in range(len(words) - 1):
        yield(words[i], words[i+1])
     
# Word pairs to keys
w_pairs = pairs_keys(words)

# Specify words dictionary to store unique key and value
w_dict = {}

for w1, w2 in w_pairs:
    # If key doesn't exists add a new key
    if w1 not in w_dict.keys():
        w_dict[w1] = [w2]
    else:
        # If key already exists update the existing value
        w_dict[w1].append(w2)
        
# Build Markov Chain model
# Get the key word 
w_first = np.random.choice(words)

# Pick the first word with the first capital letter
while w_first.islower():
    w_first = np.random.choice(words)

mk = [w_first]

# New song
# Enter word count to be your new song
w_count = 100

for i in range(w_count):
    mk.append(np.random.choice(w_dict[mk[-1]]))

# Join selected words
print(' '.join(mk))
    


