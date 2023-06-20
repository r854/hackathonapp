steps I need 
1. store data in python list 
2. create json objects out of them
3. maintain unique json object
4. scrape problem statement again from the unique json objects 
     4.1 Create a new json file and for each question a new folder with problemstatement 
     4.2 Ignore all the premium questions and please follow sequential numbering 
5. Implement TF-IDF on the Problem Statement (Not on the Question Name)

https://stackoverflow.com/questions/12293208/how-to-create-a-list-of-lists

Next Flow
  Create json file
  for each tag
    open tag in new tab and switch to that tab
    go to each tag ---> write in file 
    close and return to prev tab
  close browser

  #will do later
#TODO Error handing and retrying again part needs to be implemented
# because sometimes it was able to locate the checkbox and sometimes it isn't

#dump 1
# href_list = []
# for div_element in div_elements:
#     anchor_tags = div_element.find_elements(By.TAG_NAME, 'a')
#     for anchor_tag in anchor_tags:
#         href = anchor_tag.get_attribute('href')
#         href_list.append(href)

# # Print the list of href values
# for href in href_list:
#     print(href)

# from bs4 import BeautifulSoup
# import time
# from openpyxl import workbook
# import pandas as pd
# import os

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_experimental_option("excludeSwitches",["enable-Logging"])
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get(siteUrl)
driver.maximize_window()
WebDriverWait(driver,10)

how the functions will react 
free -
      filter(): increments index
                add it to the list of free questions
      get_problem():
                return true to filter()
                scrapes body , calls folder(),passes scraped body to it
      folder():
                creates a folder and a txt file
                writes the scraped data passed by get_problem() to the txt file
premium - 
        filter(): index remains untouched
                  list of free question untouched
                  A message is displayed on terminal that it was a free question
        get_problem():
                return false to filter()

        folder():
                this function is'nt called ,
                so no folder and file inside it will be created

Implement TF-IDF
#TODO
  prepare doc = load_Title + load_statement + join them + preprocess

  1. Prepare the documents(big strings) for the algorithm
      1.1 Load the question name from json file
      1.1.Load all the data from all .txt file and append after question name
      1.2.clean them (removal from 'Example' , format strings like /n etc)
  2. Calculate the vocab considering all the documents
      vocab = dictionary of all words 
      word vs its frequency across all the documents(=big string)
  3. Maintain an inverted index for each term (document no, frequency of the word in that doc)
  4. calculate tf(word,doc) using any 1(blog) or 2(vivek sir's) heuristic function
  5. calculate idf(word) using any 1(blog) or 2(vivek sir's) heuristic function
  6. calculate tf-idf(word,doc) = tf x idf
  7. use a ranking function 1(blog's averaging func) or 2(vivek sir's cosine similarity) heuristic function
     to calculate the rank of the document.
  8. Return the document numbers along with their score (= we can also return the json objects in this case)
_________________________________________________________________________
|                   after tf-idf implementation                          |
-------------------------------------------------------------------------|
|  documents.txt =  the absolute preprocessed version of each document   |
|  idf-values.txt = 
|  inverted-index.txt =
|  vocab.txt = 
|------------------------------------------------------------------------|
|  prepare.py = to prepare(clean+preprocess) the documents               |
|  query.py = logic to suppport/fuel query functionality in the website  |
|------------------------------------------------------------------------|

files to erect
-------------------------------------------------------------------------
chikni doc -------> vocab----->inverted index
preprocess         createvocab  create invertedindex

-------------------------------------------------------------------------------------------dumps
 # Iterate over the words in each document

    
    
# Iterate over the words in each document
    index =1
    for document in df['text']:
      # Remove occurrences of the pattern
      document = re.sub(r'\([^()]+\)|\b\w{3}-\w{4}\b|\b\w{3}-\w{3}-\w{4}\b', '', document)
      words = document.split()
      # Keep only alphabetic words
      words = [word for word in words if word.isalpha()]



#question_details = [❓,❓,❓,❓,❓,❓,❓,❓,❓,❓,❓]
#documents(=📚) = [🧾,🧾,🧾,🧾,🧾,🧾,🧾,🧾,🧾,🧾,🧾,🧾,🧾,🧾,🧾]

nltk.download('punkt')
nltk.download('stopwords')

    filepath = 'FreeLeetcode.json'
    folder = 'QData'
    question_names = load_problem_title(filepath)
    documents = load_problem_statement(folder)
    
    modified_documents = merge_title_with_statement(question_names,documents)
    print(modified_documents)








    # Print the modified dataframe
    print(df)

    for document in df['text']:
      
      # Remove occurrences of the pattern
      document = re.sub(r'\([^()]+\)|\b\w{3}-\w{4}\b|\b\w{3}-\w{3}-\w{4}\b', '', document)
      


    #save inverted index to text file
    # Open the file in write mode
    # with open('inverted_index1.txt', 'w') as file:
    #     # Iterate over the inverted index dictionary
    #     for word, postings in inverted_index.items():
    #         # Write the word and postings to the file
    #         file.write(word + ': ')
    #         file.write(', '.join(['(%d , %d)' %(idx, freq) for idx, freq in postings]))
    #         file.write('\n')
    # Path to the pickle file
    pickle_file_path = "invertedIndex.pickle"

    # Store the dictionary in the pickle file
    with open(pickle_file_path, "wb") as file:
        pickle.dump(inverted_index, file)

pip3 install -U scikit-learn scipy matplotlib


for word in vocabulary:
    tf_idf_values = []
    for doc_id in range(total_documents):
        freq = inverted_index[word].get(doc_id, 0)  # Get frequency or use default value 0
        tf = freq / document_word_count[doc_id]
        idf = math.log10(total_documents / document_frequency[word])
        tf_idf = tf * idf
        tf_idf_values.append(tf_idf)
    print(f"Word: {word}, TF-IDF Values: {tf_idf_values}")


def load_necessary_items():
    clean_doc = load_documents('clean_doc.csv')
    vocab = load_vocab('vocab.pkl')
    inverted_index = load_inverted_index('inverted_index.pkl')
    questions = load_question_details('FreeLeetcode.json')

def calculate_tf(word_frequency, document_length):
    return (word_frequency / document_length)

def calculate_idf(total_documents, document_frequency):
    return math.log10(total_documents / document_frequency)

def calculate_tf_idf(tf, idf):
    return (tf * idf)


tried removing stemming
    
    