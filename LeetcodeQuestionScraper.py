from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import json

filename = "Leetcode1.json"
totalQ = 0

siteUrl = "https://www.leetcode.com/problems/"

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_experimental_option("excludeSwitches",["enable-Logging"])

dataSet = set()
data = []

#Previously the browser was opeing and then immediately closing then I added the following line and it magically worked
#link = https://www.youtube.com/watch?v=ijT2sLVdnPM&ab_channel=GameTrick
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get(siteUrl)
driver.maximize_window()
WebDriverWait(driver,10)

#since all tags have same class name we just iterarte over them 

# driver.find_elements(By.CSS_SELECTOR,'group m-[10px] flex items-center')


# div_elements = driver.find_elements(By.CSS_SELECTOR, '.group.m-[10px].flex.items-center')
div_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "group") and contains(@class, "m-[10px]") and contains(@class, "flex") and contains(@class, "items-center")]')

print("There are %d tags in total." %(len(div_elements)))

expand = driver.find_element(By.CLASS_NAME, "grow.text-right")
expand.click()

noThanks = driver.find_elements(By.CLASS_NAME,"chakra-button.css-4obz47")
for no in noThanks:
  no.click()

for div_element in div_elements:
    #goes to every tag and opens it in new tab
  ActionChains(driver).key_down(Keys.CONTROL).click(div_element).key_up(Keys.CONTROL).perform()
    # Switch to the new tab
  driver.switch_to.window(driver.window_handles[-1])
    #wait for 4 secs to load the page properly
  wait = WebDriverWait(driver, 60)
  wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "tags-toggl__3H2x")))
    # Locate the checkbox element
  checkbox_element = driver.find_element(By.CLASS_NAME, "tags-toggl__3H2x")
    # Click the checkbox
  checkbox_element.click()
    #now the table body will have a new column named tags
    #Have to repeat for all table rows
  table_body = driver.find_element(By.CLASS_NAME,"reactable-data")
    # Find all table rows within the tbody (in here you reach to the question rows)
  table_rows = table_body.find_elements(By.TAG_NAME, "tr")
  TotalQuestions = len(table_rows)
  print("Total no of Questions = %d" %(TotalQuestions))
  totalQ += TotalQuestions
  question_no = 0
  # Iterate over the table rows
  for row in table_rows:# for every tr in tbody
    question ={}
    question_no += 1
    # Process each row as needed
    # For example, extract data from cells or perform actions on the row
    cells = row.find_elements(By.TAG_NAME, "td")
    col = 0
    for cell in cells: #for every td in tr
    # Process each cell in the row
    # Extract data or perform actions on the cell
      col+=1
      if((col == 1) or (col==5) or (col==7)):
        continue
      cell_text = cell.text
      if(col==2):
          #question no in Leetcode website
          question["number"] = cell_text
      elif(col==3):
          #question name in Leetcode website
          question["name"] = cell_text
      elif(col==4):
          # question tags
          tag = cell.find_elements(By.TAG_NAME, "a")
          Tags = []
          for t in tag:
            Tags.append(t.text)
          question["tags"] = Tags
      elif(col==6):
          #question difficulty as per mentioned in site(easy ,medium, hard)
          question["difficulty"] = cell_text
    # Find the elements using the CSS selector(I am finding the link of the question)
    question_link = "tbody>tr:nth-child(%d)>td:nth-child(3)>div>a" %(question_no)
    elements = driver.find_element(By.CSS_SELECTOR, question_link)
    href = elements.get_attribute("href")
    question["url"] = href
    data.append(question)

  # Close the current tab
  driver.close()
  # Switch back to the original tab
  driver.switch_to.window(driver.window_handles[0])
  #close browser
driver.quit()

# Save the list to a JSON file
with open(filename, 'w') as file:
  json.dump(data, file, indent=4)

print("Total Questions Scraped = %d " %(totalQ))
