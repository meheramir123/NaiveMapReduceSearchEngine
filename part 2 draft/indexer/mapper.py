#!/usr/bin/env python3

import sys
import csv
import math

# input comes from standard input
for line in sys.stdin:
    # Parse the CSV line as a document
    document_id, text = line.strip().split(",", 1)
    words = text.split()

    # Calculate term frequency (TF) for each term
    word_count = len(words)
    term_freq = {}
    for word in words:
        if word in term_freq:
            term_freq[word] += 1
        else:
            term_freq[word] = 1
    
    # Emit (term, document_id:tf) pairs
    for term, freq in term_freq.items():
        print('%s\t%s:%s' % (term, document_id, freq))

