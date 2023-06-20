#Algomate
Algomate is a free tool that allows users to search for all the free questions available on LeetCode. It was developed by Rahul Das as part of the Algozenith Hackathon under the guidance of Vivek Gupta and Prabal Jain.

##Features
Search all the free questions on LeetCode.
Utilizes TF-IDF algorithm for efficient search and ranking of documents.
Preprocessed question details and stored them in a JSON file.
Filtered and extracted unique free questions.
Implemented TF-IDF algorithm from scratch to calculate document similarity scores.
Created a Pandas DataFrame to store and process the question data.
Developed a vocabulary and inverted index to optimize search and retrieval.
Ranked documents based on similarity scores, providing a list of relevant questions.

##Keywords
Corpus: A list of all document strings (in this case, the Pandas DataFrame containing question data).
Vocabulary: A list of all unique words across the corpus.
Stop words: A list of commonly used words that do not convey special meaning pertaining to a document.

##How it Works
1.Scraping and Data Storage:

All question details are scraped and stored in a JSON file.
Unique questions are extracted and saved.
The problem statement of each free question is copied into individual text files under the QDATA folder.

2.TF-IDF Algorithm:

The TF-IDF algorithm is implemented from scratch.
Each document is created by combining the problem title and problem statement.
Documents are stored in a Pandas DataFrame.
Preprocessing steps are applied to clean the documents, such as removing non-alphanumeric characters, lowercasing, tokenizing, and removing single alphanumeric characters.
Clean documents are prepared for further processing.

3.Vocabulary and Inverted Index:

A vocabulary is created, which is a list of unique words across all documents.
An inverted index is constructed, which is a dictionary containing pairs of vocabulary terms and lists of pairs representing document IDs and the frequency of the word in each document.

4.Document Ranking:

When a search query is entered, the similarity scores of the documents are dynamically calculated based on the query terms.
The pre-calculated inverted index is used to rank the documents efficiently.
TF-IDF (Term Frequency-Inverted Document Frequency) is used for scoring the documents.
TF (word, document) is calculated as the number of times the word appears in the document divided by the total number of words in the document.
Inverted Document Frequency (word) is calculated as the logarithm of the total number of documents in the corpus divided by the number of documents the word appears in, plus one.
The effect of high-frequency stop words is nullified through this scoring process.
The similarity score of a document is calculated as the sum of TF-IDF scores for all query terms divided by the number of query terms.
The search results display a list of documents with positive scores, ranked in a non-increasing manner.

##Future Enhancements
Currently, Algomate supports searching for questions specifically on LeetCode. However, there are plans to roll out new features and support for other platforms in the future. Stay tuned for updates!

Thank you for using Algomate!