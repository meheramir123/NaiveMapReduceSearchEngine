#!/usr/bin/env python3

import sys
import csv
import json

# Initialize a set to store encountered words
encountered_words = set()

def mapper():
    for line in sys.stdin:
        # Parse CSV line
        doc_id, text = line.strip().split(',', 1)
        # Emit word count for each document
        emit_word_count(doc_id, text)

def emit_word_count(doc_id, text):
    words = text.split()
    vector_representation = {word: 1 for word in words if word in encountered_words}
    output = {
        'doc_id': doc_id,
        'vector_representation': vector_representation
    }
    print(json.dumps(output))

if __name__ == "__main__":
    mapper()

