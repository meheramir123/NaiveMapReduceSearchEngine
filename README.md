# NaiveMapReduceSearchEngine
 This repository hosts a simple implementation of a search engine utilizing the MapReduce paradigm. By leveraging MapReduce, the system can handle large datasets distributed across multiple nodes, providing scalability and fault tolerance. 
# 1) Data Processing
# Features:
1. **Data Loading:** The repository includes functions to load CSV data into Pandas DataFrames, ensuring smooth data ingestion.
2. **Data Cleaning:** It offers functionality to drop rows with missing values, ensuring data integrity and quality.
3. **Text Preprocessing:** The repository provides utilities for preprocessing textual data, including tokenization, removal of stopwords, stemming, and lemmatization.
4. **Parallel Processing:** To improve efficiency, the repository supports parallel processing of text data using concurrent.futures.
5. **Saving Preprocessed Data:** After cleaning and preprocessing, the repository allows users to save the cleaned and preprocessed data to a new CSV file.

**Usage:**
1. **Data Loading:** Users can load CSV data using the provided functions.
2. **Data Cleaning:** Easily drop rows with missing values to ensure data quality.
3. **Text Preprocessing:** Apply tokenization, stopword removal to textual data for further analysis.
4. **Save Preprocessed Data:** Save the cleaned and preprocessed data to a new CSV file for future use.

**Dependencies:**
- Python 3.x
- pandas
- nltk

**Example Usage:**
```python
# Example usage of DataProcessingRepo
from data_processing_utils import load_data, drop_missing_values, preprocess_text, parallel_preprocess, save_preprocessed_data

# Load CSV data
data = load_data('data.csv')

# Drop rows with missing values
data = drop_missing_values(data)

# Save preprocessed data to a new CSV file
save_preprocessed_data(data, 'preprocessed_data.csv')
```
# 3)MapReduce implementation for query processing

1. **Vectorizing Queries:**
   - **Mapper:** Tokenize each query text into words and emit (query_id, word) pairs with a count of 1 for each word.
   - **Reducer:** Aggregate word counts for each query to create a dictionary of word frequencies for each query.

2. **Calculating Relevance Scores:**
   - **Mapper:** Load pre-calculated query vectors and document vectors. Compute the cosine similarity between each query vector and document vector pair.
   - **Reducer:** Sum up relevance scores for each query-document pair to get the total relevance score.

3. **Ranking Relevant Documents:**
   - **Mapper:** Emit (query_id, total_score) pairs where total_score is the relevance score for each document under a query.
   - **Reducer:** Sort document relevance scores in descending order and assign ranks to documents.

4. **Retrieving Relevant Content:**
   - **Mapper:** Retrieve content for each ranked document ID.
   - **Reducer:** Aggregate and return relevant content for each query.

Each step involves a Mapper function to process input data and emit intermediate key-value pairs, and a Reducer function to aggregate and process intermediate results to produce the final output. These MapReduce jobs can be run on distributed computing framework like Hadoop allowing for efficient processing of large-scale data sets across multiple nodes.
**Acknowledgments:**
The DataProcessingRepo utilizes various open-source libraries and tools, including pandas, NLTK, and concurrent.futures, for efficient data processing and text preprocessing. Special thanks to the contributors of these projects for their valuable work.
