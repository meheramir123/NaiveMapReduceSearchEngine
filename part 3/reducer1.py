#!/usr/bin/env python3

import sys

def query_response_reducer():
    for line in sys.stdin:
        # Split the input line by tab character
        doc_id, content = line.strip().split('\t', 1)
        # Output the document ID and content
        print(f"{ARTICLE_ID}\t{SECTION_TEXT}")

if __name__ == "__main__":
    query_response_reducer()

