#!/usr/bin/env python3

import sys
import csv

# Initialize a set to store encountered words
encountered_words = set()

# input comes from standard input
for line in sys.stdin:
    # parse the CSV line
    words = line.strip().split()
    # Emit each unique word only once
    for word in words:
        if word not in encountered_words:
            encountered_words.add(word)
            print(word)
