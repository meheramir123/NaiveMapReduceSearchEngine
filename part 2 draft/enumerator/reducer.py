#!/usr/bin/env python3

import sys

# Initialize a dictionary to store word-to-ID mappings
word_to_id = {}
current_id = 0

# input comes from standard input
for line in sys.stdin:
    # Parse the input we got from the mapper
    word_set = line.strip().split()
    
    # Emit each unique word along with its unique ID
    for word in word_set:
        if word not in word_to_id:
            # Assign a new ID to the word
            word_to_id[word] = current_id
            current_id += 1
        
            # Output the word and its unique ID
            print('%s\t%s' % (word, word_to_id[word]))
