import math
import json
import numpy as np
import pickle
import prepare
import pandas as pd


def preprocess_query_string():
    query = input("What you wan't to search ?")
    query_tokens = prepare.preprocess_text_string(query)
    return query_tokens

def load_vocab(filepath):
        # Load the list from the file
    with open(filepath, 'rb') as f:
        vocab = pickle.load(f)
    return vocab

def load_inverted_index(filepath):
        # Load the dict from the file
    with open(filepath, 'rb') as f:
        inv_indx = pickle.load(f)
    return inv_indx

def load_documents(filepath):
        # Load the DataFrame from the pickle file
    with open(filepath, 'rb') as file:
        dataframe = pickle.load(file)
    return dataframe

def load_question_details(filepath):
    with open(filepath,'r') as file:
        questions = json.load(file)
    return questions

def calculate_sorted_order_of_documents(query_terms,inverted_index,documents):
    sorted_documents =[]
    total_terms = len(query_terms)
    total_documents = len(documents)
    #make a list of pair of (score,doc)
    #sort in descending order
    #return the docs with the highest score 
    score = []
    #for each query term calculate a list of tf values against each document
    for term in query_terms:
        tf_list = []
        #check if the given query word is present in vocab(inverted index in our case) or not 
            #if word is present in index calculate tf values against all docs in a tf list
        if term in inverted_index:
            for doc_id, document in documents.iterrows():
                term_frequency = 0
                for doc_term, freq in inverted_index[term]:
                    if doc_term == doc_id+1:
                        term_frequency = freq
                        break
                tf_list.append(term_frequency)

        #else tf vector is 0 vector(all terms 0)
        else:
            tf_list = [0] * total_documents

        #calculate the idf value of that term from inverted index
        # idf = math.log10(total_documents / len(inverted_index[term]))
        idf = math.log(total_documents / len(inverted_index.get(term, []))+1)

        #multiply idf of a word with the tf list of that word
        tf_idf_scores = [tf * idf for tf in tf_list]

        #take column average(calculating doc score)
        score.append(tf_idf_scores)

    score = np.array(score)
    avg_scores = np.sum(score, axis=0) / total_terms
    sorted_documents = [(score, doc_id) for doc_id, score in enumerate(avg_scores, start=1)]
    sorted_documents = sorted(sorted_documents, key=lambda x: x[0], reverse=True)
    return sorted_documents

def return_search_result(permutation):
    index = 0
    questions = load_question_details('FreeLeetcode.json')
    for score,doc_id in permutation:
       index +=1
       if index<=40:
           print('name = %s, score = %d \n' %(questions[doc_id-1]['url'],score))
       else:
           break

def main():
    clean_doc = load_documents('clean_doc.pkl')
    inverted_index = load_inverted_index('inverted_index.pkl')
    query_terms = preprocess_query_string()

    permutation = calculate_sorted_order_of_documents(query_terms,inverted_index,clean_doc)
    return_search_result(permutation)
    
if __name__ == "__main__":
    main()