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
    
    #css styles

    .table {
            width: 100%;
            margin-bottom: 1rem;
            color: #212529;
        }

        .table thead th {
            vertical-align: bottom;
            border-bottom: 2px solid #dee2e6;
        }

        .table tbody + tbody {
            border-top: 2px solid #dee2e6;
        }

        .table-bordered {
            border: 1px solid #dee2e6;
        }

        .table-bordered th,
        .table-bordered td {
            border: 1px solid #dee2e6;
        }

        .table-striped tbody tr:nth-of-type(odd) {
            background-color: rgba(0, 0, 0, 0.05);
        }

leetcode api = https://leetcode.com/graphql

https://leetcode.com/graphql?query=query
{     
  recentSubmissionList(username:"YOUR_USERNAME") {
    title
    titleSlug
    timestamp
    statusDisplay
    lang
    __typename
    }
    matchedUser(username: "YOUR_USERNAME"){
      submitStats: submitStatsGlobal {
                    acSubmissionNum {
                      difficulty
                      count
                      submissions
                        __typename
                    }
                    totalSubmissionNum {
                      difficulty
                      count
                      submissions
                       __typename
                      }
                     __typename
        }
    }    
}


    https://leetcode.com/graphql?query=query{ progressList(pageNo: 2, numPerPage: 10, filters: {}) {
  isProgressCalculated
  solvedQuestionsInfo(pageNo: $pageNo, numPerPage: $numPerPage, filters: $filters) {
    currentPage
    pageNum
    totalNum
    data {
      totalSolves
      question {
        questionFrontendId
        questionTitle
        questionDetailUrl
        difficulty
        topicTags {
          name
          slug
        }
      }
      lastAcSession {
        time
        wrongAttempts
      }
    }
  }
}
}
    
https://leetcode.com/graphql?query=query{
    query progressList(username: "rahul1999"){
    data (username: "rahul1999"){
      totalSolves
      question {
        questionFrontendId
        questionTitle
        questionDetailUrl
        difficulty
        topicTags {
          name
          slug
        }
      }
      lastAcSession {
        time
        wrongAttempts
      }
    }
    }
}

<div class="checkbox-wrapper-25">
  <input type="checkbox">
</div>

<style>
  .checkbox-wrapper-25 input[type="checkbox"] {
    background-image: -webkit-linear-gradient(hsla(0,0%,0%,.1), hsla(0,0%,100%,.1)),
                      -webkit-linear-gradient(left, #f66 50%, #6cf 50%);
    background-size: 100% 100%, 200% 100%;
    background-position: 0 0, 15px 0;
    border-radius: 25px;
    box-shadow: inset 0 1px 4px hsla(0,0%,0%,.5),
                inset 0 0 10px hsla(0,0%,0%,.5),
                0 0 0 1px hsla(0,0%,0%,.1),
                0 -1px 2px 2px hsla(0,0%,0%,.25),
                0 2px 2px 2px hsla(0,0%,100%,.75);
    cursor: pointer;
    height: 25px;
    padding-right: 25px;
    width: 75px;
    -webkit-appearance: none;
    -webkit-transition: .25s;
}
.checkbox-wrapper-25 input[type="checkbox"]:after {
    background-color: #eee;
    background-image: -webkit-linear-gradient(hsla(0,0%,100%,.1), hsla(0,0%,0%,.1));
    border-radius: 25px;
    box-shadow: inset 0 1px 1px 1px hsla(0,0%,100%,1),
                inset 0 -1px 1px 1px hsla(0,0%,0%,.25),
                0 1px 3px 1px hsla(0,0%,0%,.5),
                0 0 2px hsla(0,0%,0%,.25);
    content: '';
    display: block;
    height: 25px;
    width: 50px;
}
.checkbox-wrapper-25 input[type="checkbox"]:checked {
    background-position: 0 0, 35px 0;
    padding-left: 25px;
    padding-right: 0;
}
</style>

    thead th {
      background-color: #f8f9fa; /* Set the background color */
      border-color: #dee2e6; /* Set the border color */
      color: #212529; /* Set the font color */
      font-weight: bold; /* Apply bold font weight */
      text-transform: uppercase; /* Convert text to uppercase */
    }


FAancy search
    <div class="search-box">
      <div class="search-icon"><i class="fa fa-search search-icon"></i></div>
      <form action="" class="search-form">
        <input type="text" placeholder="Search" id="search" autocomplete="off">
      </form>
      <svg class="search-border" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:a="http://ns.adobe.com/AdobeSVGViewerExtensions/3.0/" x="0px" y="0px" viewBox="0 0 671 111" style="enable-background:new 0 0 671 111;"
       xml:space="preserve">
          <path class="border" d="M335.5,108.5h-280c-29.3,0-53-23.7-53-53v0c0-29.3,23.7-53,53-53h280"/>
          <path class="border" d="M335.5,108.5h280c29.3,0,53-23.7,53-53v0c0-29.3-23.7-53-53-53h-280"/>
        </svg>
      <div class="go-icon"><i class="fa fa-arrow-right"></i></div>
    </div>

  
  css
  *, *:before, *:after {
  -webkit-tap-highlight-color: transparent;
  -webkit-tap-highlight-color: rgba(0,0,0,0);
  user-select: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  -o-user-select: none;
  box-sizing: border-box;
  -webkit-box-sizing: border-box;
  padding: 0;
  margin: 0;
}
a, a:visited, a:hover {
  color: inherit;
  text-decoration: none;
}
main {
  position: absolute;
  top: 0;
  left: 0;
  margin: 0 auto;
  padding: 0 26px;
  width: 100%;
  height: 100%;
  background: rgba(154,57,163,1);
  background: -moz-linear-gradient(-45deg, rgba(154,57,163,1) 0%, rgba(65,103,168,1) 100%);
  background: -webkit-gradient(left top, right bottom, color-stop(0%, rgba(154,57,163,1)), color-stop(100%, rgba(65,103,168,1)));
  background: -webkit-linear-gradient(-45deg, rgba(154,57,163,1) 0%, rgba(65,103,168,1) 100%);
  background: -o-linear-gradient(-45deg, rgba(154,57,163,1) 0%, rgba(65,103,168,1) 100%);
  background: -ms-linear-gradient(-45deg, rgba(154,57,163,1) 0%, rgba(65,103,168,1) 100%);
  background: linear-gradient(135deg, rgba(154,57,163,1) 0%, rgba(65,103,168,1) 100%);
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#9a39a3', endColorstr='#4167a8', GradientType=1 );
}
h1 {
  display: block;
  margin: 0 auto 25px auto;
  text-align: center;
  font-size: 1.92em;
  font-weight: 600;
  letter-spacing: -0.055em;
}
h2 {
  display: block;
  margin: 0 auto 60px auto;
  text-align: center;
  font-weight: 400;
  font-size: 1.25em;
  letter-spacing: -0.015em;
}
.container {
  position: relative;
  margin: calc(75px + 2vh + 2vw) auto 0 auto;
  padding: 0;
  width: 100%;
  max-width: 840px;
}
.search-box {
  position: relative;
  width: 100%;
  max-width: 360px;
  height: 60px;
  border-radius: 120px;
  margin: 0 auto;
}
.search-icon, .go-icon {
  position: absolute;
  top: 0;
  height: 60px;
  width: 86px;
  line-height: 61px;
  text-align: center;
}
.search-icon {
  left: 0;
  pointer-events: none;
  font-size: 1.22em;
  will-change: transform;
  transform: rotate(-45deg);
  -webkit-transform: rotate(-45deg);
  -moz-transform: rotate(-45deg);
  -o-transform: rotate(-45deg);
  transform-origin: center center;
  -webkit-transform-origin: center center;
  -moz-transform-origin: center center;
  -o-transform-origin: center center;
  transition: transform 400ms 220ms cubic-bezier(0.190, 1.000, 0.220, 1.000);
  -webkit-transition: transform 400ms 220ms cubic-bezier(0.190, 1.000, 0.220, 1.000);
  -moz-transition: transform 400ms 220ms cubic-bezier(0.190, 1.000, 0.220, 1.000);
  -o-transition: transform 400ms 220ms cubic-bezier(0.190, 1.000, 0.220, 1.000);
}
.si-rotate {
  transform: rotate(0deg);
  -webkit-transform: rotate(0deg);
  -moz-transform: rotate(0deg);
  -o-transform: rotate(0deg);
}
.go-icon {
  right: 0;
  pointer-events: none;
  font-size: 1.38em;
  will-change: opacity;
  cursor: default;
  opacity: 0;
  transform: rotate(45deg);
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -o-transform: rotate(45deg);
  transition: opacity 190ms ease-out, transform 260ms cubic-bezier(0.190, 1.000, 0.220, 1.000);
  -webkit-transition: opacity 190ms ease-out, transform 260ms cubic-bezier(0.190, 1.000, 0.220, 1.000);
  -moz-transition: opacity 190ms ease-out, transform 260ms cubic-bezier(0.190, 1.000, 0.220, 1.000);
  -o-transition: opacity 190ms ease-out, transform 260ms cubic-bezier(0.190, 1.000, 0.220, 1.000);
}
.go-in {
  opacity: 1;
  pointer-events: all;
  cursor: pointer;
  transform: rotate(0);
  -webkit-transform: rotate(0);
  -moz-transform: rotate(0);
  -o-transform: rotate(0);
  transition: opacity 190ms ease-out, transform 260ms 20ms cubic-bezier(0.190, 1.000, 0.220, 1.000);
  -webkit-transition: opacity 190ms ease-out, transform 260ms 20ms cubic-bezier(0.190, 1.000, 0.220, 1.000);
  -moz-transition: opacity 190ms ease-out, transform 260ms 20ms cubic-bezier(0.190, 1.000, 0.220, 1.000);
  -o-transition: opacity 190ms ease-out, transform 260ms 20ms cubic-bezier(0.190, 1.000, 0.220, 1.000);
}
.search-border {
  display: block;
  width: 100%;
  max-width: 360px;
  height: 60px;
}
.border {
  fill: none;
  stroke: #FFFFFF;
  stroke-width: 5;
  stroke-miterlimit: 10;
}
.border {
  stroke-dasharray: 740;
  stroke-dashoffset: 0;
  transition: stroke-dashoffset 400ms cubic-bezier(0.600, 0.040, 0.735, 0.990);
  -webkit-transition: stroke-dashoffset 400ms cubic-bezier(0.600, 0.040, 0.735, 0.990);
  -moz-transition: stroke-dashoffset 400ms cubic-bezier(0.600, 0.040, 0.735, 0.990);
  -o-transition: stroke-dashoffset 400ms cubic-bezier(0.600, 0.040, 0.735, 0.990);
}
.border-searching .border {
  stroke-dasharray: 740;
  stroke-dashoffset: 459;
  transition: stroke-dashoffset 650ms cubic-bezier(0.755, 0.150, 0.205, 1.000);
  -webkit-transition: stroke-dashoffset 650ms cubic-bezier(0.755, 0.150, 0.205, 1.000);
  -moz-transition: stroke-dashoffset 650ms cubic-bezier(0.755, 0.150, 0.205, 1.000);
  -o-transition: stroke-dashoffset 650ms cubic-bezier(0.755, 0.150, 0.205, 1.000);
}
#search {
  font-family: 'Montserrat Alternates', sans-serif;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 120px;
  border: none;
  background: rgba(255,255,255,0);
  padding: 0 68px 0 68px;
  color: #FFFFFF;
  font-size: 1.32em;
  font-weight: 400;
  letter-spacing: -0.015em;
  outline: none;
}
#search::-webkit-input-placeholder {color: #FFFFFF;}
#search::-moz-placeholder {color: #FFFFFF;}
#search:-ms-input-placeholder {color: #FFFFFF;}
#search:-moz-placeholder {color: #FFFFFF;}
#search::-moz-selection {color: #FFFFFF; background: rgba(0,0,0,0.25);}
#search::selection {color: #FFFFFF; background: rgba(0,0,0,0.25);}

js
$(document).ready(function(){
    $("#search").focus(function() {
      $(".search-box").addClass("border-searching");
      $(".search-icon").addClass("si-rotate");
    });
    $("#search").blur(function() {
      $(".search-box").removeClass("border-searching");
      $(".search-icon").removeClass("si-rotate");
    });
    $("#search").keyup(function() {
        if($(this).val().length > 0) {
          $(".go-icon").addClass("go-in");
        }
        else {
          $(".go-icon").removeClass("go-in");
        }
    });
    $(".go-icon").click(function(){
      $(".search-form").submit();
    });
});

william scott's prepare.py
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

Prepare.py
import os
import json
import pandas as pd
import numpy as np
import nltk
import pickle
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def load_problem_title(filepath):
    # Load JSON data from LeetcodeUnique.json
    question_names = []
    with open(filepath,'r') as file:
        question_details = json.load(file)    
    
    for question in question_details:
        question_names.append(question["name"])
    return question_names

def test_load_problem_title():
    filepath = 'FreeLeetcode.json'
    question_names = load_problem_title(filepath)
    for index, name in enumerate(question_names, start=1):
        print(f"{index}. {name}")

def load_problem_statement(folder):
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
    df = pd.DataFrame(documents,columns=['body'])
    return df

def test_load_problem_statement():
    folder = 'QData'
    documents = load_problem_statement(folder)
    #iterate over every document in the list of diocuments and print it word-by-word
    for index,document in enumerate(documents['text'],start=1):
        words = document.split()
        print("Words in document %d: %s\n" %(index,words))
    
def merge_title_with_statement(question_names,df):
    #TODO : Iterate over the question_details list and merge question_details[i]["name"] to each data column in data frame df
    # Append each row of the DataFrame with the corresponding string from the list
    df['text'] = [f'{string} {text}' for text, string in zip(df['text'], question_names)]
    return df

def test_merge():
    filepath = 'FreeLeetcode.json'
    folder = 'QData'
    question_names = load_problem_title(filepath)
    documents = load_problem_statement(folder)
    modified_documents = merge_title_with_statement(question_names,documents)
    for index,document in enumerate(modified_documents['text'],start=1):
        words = document.split()
        print("Words in document %d: %s\n" %(index,words))

def prepare_documents():
    filepath = 'filtering/FreeLeetcode.json'
    folder = '../QData'
    question_names = load_problem_title(filepath)
    documents = load_problem_statement(folder)
    modified_documents = merge_title_with_statement(question_names,documents)
    return modified_documents

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

    return tokens

def preprocess_documents(df):
    #TODO : every preprocessing will happen in each row of df and will be stored there
    
    #trimming the sample testcase ,explanations etc
    df['text'] = df['text'].str.split('Example', n=1, expand=True)[0].str.strip()

    # Apply preprocessing to the dataframe
    df['text'] = df['text'].apply(preprocess_text_string)

    return df
   
def create_vocab(df):
    
    all_words = [word for doc in df['text'] for word in doc]
    vocab = sorted(set(all_words))
    return vocab

def create_invertedIndex(df):
    #TODO token --->{ (doc1,freq1),(doc2,freq2),(doc3,freq3),(doc4,freq4)}
    inverted_index = {}
    for idx, document in enumerate(df['text'],start=1): 
        word_freq = {}
        for word in document:   # frequency of all words in a document
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
        
        for word, freq in word_freq.items():  #append the frequency of the word the word's list 
            if word in inverted_index:
                inverted_index[word].append((idx, freq))
            else:
                inverted_index[word] = [(idx, freq)]
    return inverted_index

#storing in files

def store_documents(df,filepath):
        # Store the DataFrame in a pickle file
    # with open(filepath, 'wb') as file:
    #     pickle.dump(df, file)
    # Convert the DataFrame to a string representation
    df_str = df.to_string(header=False, index=False)

    # Open the text file in write mode
    with open('dataframe.txt', 'w') as file:
        # Write the DataFrame string to the file
        file.write(df_str)
    
def store_vocab(vocab,filepath):

    # Save the list to a file
    with open(filepath, 'wb') as f:
        pickle.dump(vocab, f)

def store_inverted_index(inv_indx,file_path):
    # # Assuming 'vocab' is your vocabulary object
    # with open(file_path, 'wb') as f:
    #     pickle.dump(inv_indx, f)
    # Open the text file in write mode
    with open('inverted_indexf.txt', 'w') as file:
        # Iterate over the key-value pairs of the inverted index
        for term, postings in inv_indx.items():
            # Convert the postings to a string representation
            postings_str = ', '.join([f'(doc # = {doc}, freq = {freq})' for doc, freq in postings])
            # Write the term and its postings to the file
            file.write(f'{term}: {postings_str}\n')

def main():
    documents = prepare_documents()
    store_documents(documents,'unclean_doc.pkl')

    cleaned_documents = preprocess_documents(documents)
    store_documents(cleaned_documents,'clean_doc.pkl')

    vocab = create_vocab(cleaned_documents)
    print (vocab)
    print(len(vocab))
    store_vocab(vocab,'vocab.pkl')

    inv_indx = create_invertedIndex(cleaned_documents)
    store_inverted_index(inv_indx,'inverted_index.pkl')
    
if __name__ == "__main__":
    main()



    # Open the text file in write mode
    with open('inverted_indexf.txt', 'w') as file:
        # Iterate over the key-value pairs of the inverted index
        for term, postings in inv_indx.items():
            # Convert the postings to a string representation
            postings_str = ', '.join([f'(doc # = {doc}, freq = {freq})' for doc, freq in postings])
            # Write the term and its postings to the file
            file.write(f'{term}: {postings_str}\n')

# Open the text file in write mode
    with open('dataframe.txt', 'w') as file:
        # Write the DataFrame string to the file
        file.write(df_str)