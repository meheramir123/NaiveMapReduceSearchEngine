This repository hosts a search engine implementation that utilizes the MapReduce paradigm for efficient processing of large datasets. The system comprises several components, including:

1. **Data Processing:**
   - Features data loading, cleaning, and text preprocessing functionalities using Pandas and NLTK libraries.
   - Supports parallel processing for improved efficiency.

2. **MapReduce Implementation for Indexing:**
   - **Word Enumeration and Unique Word ID Assignment:**
     - Mapper: Tokenizes each document's text and emits (word, document_id) pairs.
     - Reducer: Aggregates document IDs for each word.
   - **Calculating TF/IDF Weights for Each Term:**
     - Mapper: Tokenizes text and calculates TF, emitting (word, (doc_id, tf)) pairs.
     - Reducer: Aggregates TF values and computes IDF, resulting in TF/IDF weights for each term.
   - **Generating Index for Entire Document Corpus:**
     - Mapper: Parses TF/IDF output and emits (word, (doc_id, tfidf)) pairs.
     - Reducer: Aggregates TFIDF values, yielding an index structure.

3. **MapReduce Implementation for Query Processing:**
   - **Vectorizing Queries:**
     - Mapper: Tokenizes query text and emits (query_id, word) pairs.
     - Reducer: Aggregates word frequencies for each query.
   - **Calculating Relevance Scores:**
     - Mapper: Computes cosine similarity between query and document vectors.
     - Reducer: Sums relevance scores for each query-document pair.
   - **Ranking Relevant Documents:**
     - Mapper: Emits (query_id, total_score) pairs for ranking.
     - Reducer: Sorts and ranks documents based on relevance scores.
   - **Retrieving Relevant Content:**
     - Mapper: Retrieves content for ranked documents.
     - Reducer: Aggregates and returns relevant content for each query.

These MapReduce jobs efficiently handle large-scale data processing across distributed computing nodes. The system facilitates tasks such as document indexing, query processing, relevance ranking, and content extraction. Each component plays a crucial role in the search engine's functionality, ensuring effective information retrieval from the text corpus.

**Acknowledgments:**
This project utilizes open-source libraries and tools such as pandas, NLTK, and concurrent.futures for data processing and text analysis. 
