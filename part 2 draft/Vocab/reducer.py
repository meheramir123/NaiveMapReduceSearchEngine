#!/usr/bin/env python3

import sys

# Initialize a dictionary to store word-to-document-count mappings
word_to_doc_count = {}

# input comes from standard input
for line in sys.stdin:
    # Parse the input we got from the mapper
    word, count = line.strip().split('\t')
    count = int(count)
    
    # Accumulate the count of documents for each word
    if word in word_to_doc_count:
        word_to_doc_count[word] += count
    else:
        word_to_doc_count[word] = count

# Output the word and its document count
for word, doc_count in word_to_doc_count.items():
    print('%s\t%s' % (word, doc_count))

