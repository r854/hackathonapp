import os
import json
import pandas as pd
import numpy as np
import nltk
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer
from collections import Counter

docFreq= {}
tf_idf={}
tf_idf_title={}
def load_problem_title(filepath):
    # Load JSON data from LeetcodeUnique.json
    question_names = []
    with open(filepath,'r') as file:
        question_details = json.load(file)    
    
    for question in question_details:
        question_names.append(question["name"])
    
    df = pd.DataFrame(question_names,columns=['title'])
    return df

def load_problem_statement(folder,df):
    documents=[]
    data_path = os.path.join(os.getcwd(), folder)

    for folder_num in range(1,2163):
        folder_path = os.path.join(data_path, str(folder_num))
        file_path = os.path.join(folder_path, str(folder_num) + ".txt")
        
        # Read the contents of the text file
        with open(file_path, "r",encoding="utf-8") as file:
            text = file.read()
        
        # Perform further processing with the text
        # (e.g., tokenize, preprocess, etc.)
        documents.append(text)
    df ['body'] = documents
    return df

def preprocess_text_string(text):
    
    # Convert to lowercase
    text = text.lower()
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove non-alphanumeric tokens
    tokens = [token for token in tokens if token.isalnum()]

    # Remove numbers that are standalone
    tokens = [token for token in tokens if not token.isdigit()]

    # Remove single-character tokens
    tokens = [token for token in tokens if len(token) > 1]

    # Stemming
    # Initialize the stemmer
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]

    return tokens

def preprocess_documents(df):
    #TODO : every preprocessing will happen in each row of df and will be stored there
    
    #trimming the sample testcase ,explanations etc
    df['body'] = df['body'].str.split('Example', n=1, expand=True)[0].str.strip()

    # Apply preprocessing to the dataframe
    df['clean_title'] = df['title'].apply(preprocess_text_string)
    df['clean_body'] = df['body'].apply(preprocess_text_string)

    return df

def inverted_index(df):

    for index,document in enumerate(df['clean_title'],start=1):
        for word in document:
            try:
                docFreq[word].add(index)
            except:
                docFreq[word] = {index}

    for index,document in enumerate(df['clean_body'],start=1):
        for word in document:
            try:
                docFreq[word].add(index)
            except:
                docFreq[word] = {index}
    print(docFreq)  

def merge_title_body(df):
    # Merge corresponding elements of columns A and B into a new column C
  df['clean_doc'] = [a + b for a, b in zip(df['clean_title'], df['clean_body'])]

def doc_freq(word):
    c = 0
    try:
        c = doc_freq[word]
    except:
        pass
    return c

def calculate_tf_body(df):
    
    documents = df['clean_doc']
    for index,body in enumerate(df['clean_body']):
        total_words = len(documents[index])
        counter = Counter(documents[index])

        for token in np.unique(documents[index]):
            tf = counter[token]/total_words
            d_f = doc_freq(token)
            idf = np.log(len(documents)/(d_f+1))
            tf_idf[index, token] = tf*idf

def calculate_tf_head(df):
    documents = df['clean_doc']
    for index,body in enumerate(df['clean_title']):
        total_words = len(documents[index])
        counter = Counter(documents[index])

        for token in np.unique(documents[index]):
            tf = counter[token]/total_words
            d_f = doc_freq(token)
            idf = np.log(len(documents)+1/(d_f+1))
            tf_idf_title[index, token] = tf*idf

def preprocess_query_string():
    query = input("What you wan't to search ?")
    query_tokens = preprocess_text_string(query)
    return query_tokens

def calculate_sorted_order_of_documents(query_terms):
    query_weights = {}

    for key in tf_idf:
        
        if key[1] in query_terms:
            try:
                query_weights[key[0]] += tf_idf[key]
            except:
                query_weights[key[0]] = tf_idf[key]
    
    query_weights = sorted(query_weights.items(), key=lambda x: x[1], reverse=True)
    
    l = []
    
    for i in query_weights[:40]:
        l.append(i[0])

    questions = load_question_details('../AZ HACKATHON 2023/FreeLeetcode.json')
    for doc_id in l:
      print('name = %s \n' %(questions[doc_id-1]['name']))



def load_question_details(filepath):
    with open(filepath,'r') as file:
        questions = json.load(file)
    return questions


df = load_problem_title('../AZ HACKATHON 2023/FreeLeetcode.json')
df = load_problem_statement('../AZ HACKATHON 2023/QData',df)
df = preprocess_documents(df)
merge_title_body(df)

calculate_tf_body(df)
calculate_tf_head(df)

for i in tf_idf:
    tf_idf[i] *=0.3

for i in tf_idf:
    tf_idf[i] = tf_idf_title[i]

token = preprocess_query_string()
calculate_sorted_order_of_documents(token)
