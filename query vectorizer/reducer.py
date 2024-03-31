#!/usr/bin/env python3

import sys
import json

def reducer():
    vectorized_queries = {}
    for line in sys.stdin:
        data = json.loads(line)
        query_id = data['query_id']
        vector_representation = data['vector_representation']
        if query_id not in vectorized_queries:
            vectorized_queries[query_id] = []
        vectorized_queries[query_id].append(vector_representation)

    for query_id, vector_representations in vectorized_queries.items():
        average_vector = calculate_average_vector(vector_representations)
        print(f"{query_id},{average_vector}")

def calculate_average_vector(vectors):
    num_vectors = len(vectors)
    vector_sum = {}
    for vector in vectors:
        for key, value in vector.items():
            vector_sum[key] = vector_sum.get(key, 0) + value
    average_vector = {key: value / num_vectors for key, value in vector_sum.items()}
    return average_vector

if __name__ == "__main__":
    reducer()

