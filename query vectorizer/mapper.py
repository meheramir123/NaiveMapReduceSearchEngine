#!/usr/bin/env python3

import sys
import csv
import json

def mapper():
    for line in sys.stdin:
        query_id, query = line.strip().split(',', 1)
        vector_representation = vectorize_query(query)
        output = {
            'query_id': query_id,
            'vector_representation': vector_representation
        }
        print(json.dumps(output))

def vectorize_query(query):
    words = query.split()
    vector_representation = {word: 1 for word in words}
    return vector_representation

if __name__ == "__main__":
    mapper()

