#!/usr/bin/env python3

import sys
import csv

# Initialize a set to store encountered words
encountered_words = set()

# input comes from standard input
for line in sys.stdin:
    # parse the CSV line
    words = line.strip().split()
    # Emit each unique word along with a document ID
    for word in words:
        if word not in encountered_words:
            encountered_words.add(word)
            print('%s\t%s' % (word, 1))  # Emit word with count 1 for each document

