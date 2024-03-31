#!/usr/bin/env python3

import sys
import csv

def query_response_mapper():
    reader = csv.reader(sys.stdin)
    for row in reader:
        # Extract document ID and content from CSV row
        ARTICLE_ID, SECTION_TEXT = row
        # Emit the document ID and content
        print(f"{ARTICLE_ID}\t{SECTION_TEXT}")

if __name__ == "__main__":
    query_response_mapper()

