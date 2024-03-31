#!/usr/bin/env python3

import sys
import math

def ranker_mapper():
    for line in sys.stdin:
        # Split the input line by tab character
        query_id, query = line.strip().split(',', 1)
        # Tokenize the query and emit (query_id, word) pairs
        for word in query.split():
            print(f"{query_id}\t{word}")

if __name__ == "__main__":
    ranker_mapper()

