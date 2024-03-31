#!/usr/bin/env python3

import sys

def ranker_reducer():
    current_query = None
    words = []

    for line in sys.stdin:
        # Split the input line by tab character
        query_id, word = line.strip().split('\t', 1)

        # If it's a new query, emit the aggregated list of words for the previous query
        if current_query and query_id != current_query:
            print(f"{current_query}\t{','.join(words)}")
            words = []

        current_query = query_id
        words.append(word)

    # Emit the last query's aggregated list of words
    if current_query:
        print(f"{current_query}\t{','.join(words)}")

if __name__ == "__main__":
    ranker_reducer()

