# NaiveMapReduceSearchEngine
 This repository hosts a simple implementation of a search engine utilizing the MapReduce paradigm. By leveraging MapReduce, the system can handle large datasets distributed across multiple nodes, providing scalability and fault tolerance. 
# Data Processing
# Features:
1. **Data Loading:** The repository includes functions to load CSV data into Pandas DataFrames, ensuring smooth data ingestion.
2. **Data Cleaning:** It offers functionality to drop rows with missing values, ensuring data integrity and quality.
3. **Text Preprocessing:** The repository provides utilities for preprocessing textual data, including tokenization, removal of stopwords, stemming, and lemmatization.
4. **Parallel Processing:** To improve efficiency, the repository supports parallel processing of text data using concurrent.futures.
5. **Saving Preprocessed Data:** After cleaning and preprocessing, the repository allows users to save the cleaned and preprocessed data to a new CSV file.

**Usage:**
1. **Data Loading:** Users can load CSV data using the provided functions.
2. **Data Cleaning:** Easily drop rows with missing values to ensure data quality.
3. **Text Preprocessing:** Apply tokenization, stopword removal, stemming, and lemmatization to textual data for further analysis.
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

**Acknowledgments:**
The DataProcessingRepo utilizes various open-source libraries and tools, including pandas, NLTK, and concurrent.futures, for efficient data processing and text preprocessing. Special thanks to the contributors of these projects for their valuable work.
