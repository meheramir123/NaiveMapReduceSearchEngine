#!/usr/bin/env python3

import sys
import json

# Initialize a dictionary to store document vector representations
doc_vectors = {}

def reducer():
    for line in sys.stdin:
        data = json.loads(line)
        doc_id = data['doc_id']
        vector_representation = data['vector_representation']
        # Aggregate word counts for each document
        accumulate_word_counts(doc_id, vector_representation)

    for doc_id, vector_representation in doc_vectors.items():
        relevance = calculate_relevance(vector_representation)
        print(f"doc {doc_id}: {relevance:.4f}")

def accumulate_word_counts(doc_id, vector_representation):
    if doc_id in doc_vectors:
        for word, count in vector_representation.items():
            if word in doc_vectors[doc_id]:
                doc_vectors[doc_id][word] += count
            else:
                doc_vectors[doc_id][word] = count
    else:
        doc_vectors[doc_id] = vector_representation

def calculate_relevance(vector_representation):
    relevance = 0
    for word, count in vector_representation.items():
        relevance += count  # Assuming di=1 for simplicity
    return relevance

if __name__ == "__main__":
    reducer()

