from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import json
import os
#MOTT0 = Filter free ones from the total (free + premium) and if free then copy Problem statement to  folder QDATA

filepath = "cleaning/LeetcodeUnique.json"
QDATA_FOLDER = "../QData"

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_experimental_option("excludeSwitches",["enable-Logging"])
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def filter_free_questions(data):
    #TODO 
    # input = list of all (questions as dictionary)
    # action = writes json object to leetcodefree file
    # output =list of all free (questions as dictionary)
    index = 1
    free = []
    premium = []
    for question in data:
        link = question["url"]
        success = get_problem_statement(link,index)
        if(success):
            #add that json object in LeetcodeFree.json
            free.append(question)
            index+=1 #number got booked by the free question
        else:
            premium.append(question)
            print("Premium Question : %s" %(question["url"]))
    write_free_question_to_file(free)
    write_premium_question_to_file(premium)

def get_problem_statement(link,index):
    #TODO
    # it gets called by the preceding function
    #input = gets a link of the general question
    #action = if accessable report it to caller, else also report that to caller
    #output = creates a folder with a problem statement text with in that
    #goes to each link and scrapes the problem statement
    headingClass = ".mr-2.text-label-1"
    bodyClass = ".px-5.pt-4"
    try:
        driver.get(link)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, bodyClass)))
        time.sleep(1)
        problemTitle = driver.find_element(By.CSS_SELECTOR,headingClass)
        problemStatement = driver.find_element(By.CSS_SELECTOR,bodyClass)
        print(problemTitle.text)
        if(problemTitle.text):
            create_folder_for_free_question(str(index),problemStatement.text)
        time.sleep(1)
        return True
    except Exception as e: #Will only get triggered for Premium questions
        print(e)
    return False

def create_folder_for_free_question(fileName,text):
    
    folderPath = os.path.join(QDATA_FOLDER,fileName)
    os.makedirs(folderPath,exist_ok=True)
    filePath = os.path.join(folderPath, fileName + ".txt")
    with open(filePath,'w',encoding="utf-8",errors="ignore") as newfile:
        newfile.write(text)     

def write_free_question_to_file(free):
    with open("FreeLeetcode.json", "w") as file:
    # Write the data to the file
      json.dump(free, file,indent=4)

def write_premium_question_to_file(premium):
    with open("PremiumLeetcode.json", "w") as file:
    # Write the data to the file
      json.dump(premium, file,indent=4)

def main():
    # Main logic of your program goes here
    json_file_path = filepath
    allQuestions = load_json_file(json_file_path)
    filter_free_questions(allQuestions)
    driver.quit()

if __name__ == "__main__":
    # Call the main function
    main()