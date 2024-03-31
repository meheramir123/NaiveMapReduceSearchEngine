#!/usr/bin/env python3

import sys
import math

# Initialize variables for IDF calculation
term_document_count = {}

# input comes from standard input
for line in sys.stdin:
    # Parse the input we got from the mapper
    parts = line.strip().split('\t')
    
    # Ensure the line has at least two parts
    if len(parts) != 2:
        continue
    
    term, doc_tf = parts
    
    # Split doc_tf into document_id and tf
    doc_tf_parts = doc_tf.split(':', 1)
    
    # Ensure doc_tf has two parts
    if len(doc_tf_parts) != 2:
        continue
    
    document_id, tf = doc_tf_parts
    
    # Convert tf to an integer
    try:
        tf = int(tf)
    except ValueError:
        continue

    # Update document count for the term
    if term in term_document_count:
        term_document_count[term] += 1
    else:
        term_document_count[term] = 1

# Calculate total number of documents
total_documents = len(set(document_id for term, doc_tf in (line.strip().split('\t', 1) for line in sys.stdin) for document_id, _ in [doc_tf.split(':', 1)]))

# Calculate IDF for each term and compute TF/IDF representation
for line in sys.stdin:
    # Parse the input we got from the mapper
    parts = line.strip().split('\t')
    
    # Ensure the line has at least two parts
    if len(parts) != 2:
        continue
    
    term, doc_tf = parts
    
    # Split doc_tf into document_id and tf
    doc_tf_parts = doc_tf.split(':', 1)
    
    # Ensure doc_tf has two parts
    if len(doc_tf_parts) != 2:
        continue
    
    document_id, tf = doc_tf_parts
    
    # Convert tf to an integer
    try:
        tf = int(tf)
    except ValueError:
        continue

    # Calculate IDF
    if term in term_document_count:
        idf = math.log(total_documents / term_document_count[term])
    else:
        continue

    # Calculate TF/IDF
    tfidf = tf * idf

    # Emit (document_id, {term:tfidf}) tuples
    print('%s\t{%s:%s}' % (document_id, term, tfidf))

