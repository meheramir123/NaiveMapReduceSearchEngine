#!/usr/bin/env python3

import sys
import math

# Initialize variables for IDF calculation
total_documents = 0
term_document_count = {}

# input comes from standard input
for line in sys.stdin:
    # Parse the input we got from the mapper
    term, doc_tf = line.strip().split('\t', 1)
    document_id, tf = doc_tf.split(':', 1)
    tf = int(tf)

    # Update document count for the term
    if term in term_document_count:
        term_document_count[term] += 1
    else:
        term_document_count[term] = 1

    # Emit (document_id, {term:tfidf}) tuples
    print('%s\t%s:%s' % (document_id, term, tf))

# Calculate total number of documents
total_documents = len(set([doc_id for doc_id, _ in (line.split('\t', 1)[1].split(':', 1) for line in sys.stdin)]))

# Calculate IDF for each term and compute TF/IDF representation
for line in sys.stdin:
    document_id, term_tfidf = line.strip().split('\t', 1)
    term, tf = term_tfidf.split(':', 1)
    tf = int(tf)

    # Calculate IDF
    idf = math.log(total_documents / term_document_count[term])

    # Calculate TF/IDF
    tfidf = tf * idf

    # Emit (document_id, {term:tfidf}) tuples
    print('%s\t{%s:%s}' % (document_id, term, tfidf))

