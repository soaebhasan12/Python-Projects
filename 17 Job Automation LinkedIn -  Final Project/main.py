import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install()),
    options = options
)



job_application_url = "https://www.linkedin.com/jobs/search-results/?f_AL=true&keywords=Marketing%20Intern&origin=JOBS_HOME_SEARCH_BUTTON"

driver.get(job_application_url)


time.sleep(5)

load_dotenv(dotenv_path="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/Day-49 Automating Job Applications on LinkedIn/Day-49 Automating Job Applications on LinkedIn/00 Staged Learning with Challenges/credit.env", override=True)




ACCOUNT_EMAIL = os.getenv("USERNAME")
ACCOUNT_PASSWORD = os.getenv("PASSWORD")
PHONE = os.getenv("CONTACT")




username = driver.find_element(By.NAME, "session_key")
username.click()
username.send_keys(os.getenv("USERNAME"))
password = driver.find_element(By.NAME, "session_password")
password.click()
password.send_keys(os.getenv("PASSWORD"))
SignIn = driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button")
SignIn.click()



time.sleep(5)

all_listing = driver.find_elements(By.CSS_SELECTOR, "#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__list.jobs-semantic-search-list > ul > li")

for listing in all_listing:
    print("called")
    listing.click()
    time.sleep(2)

    #try to locate the apply button if can't then skip the job.
    try:
        apply_button = driver.find_element(By.ID, "jobs-apply-button-id")
        # apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
        apply_button.click()
        time.sleep(5)

        #If phone field is empty then fill your phone number
        phone = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
        phone.clear()
        if phone.get_attribute("value") == "":
            phone.send_keys(PHONE)

        

        

        submit_button = driver.find_element(By.CSS_SELECTOR, "button.artdeco-button--primary")
        submit_button.click()

        #If the submit_button is "Next" button, then this is multi-step application, so skip.
        # if submit_button.get_attribute("data-control-name") == "continue_unify":
        if "Next" in submit_button.text:
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
            discard_button.click()
            print("Complex Application Skipped.")
            continue
        else:
            submit_button.click()
        
        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal--dismiss")
        close_button.click()
    
    #if already applied to job or job is no longer accepting application, then skip
    except NoSuchElementException:
        print("No Application Button, Skipped.")
        continue
















# #Locate the apply button
# time.sleep(5)
# apply_button = driver.find_element(By.ID, "jobs-apply-button-id")
# apply_button.click()

# #If application requires phone number and the field is empty, then fill in the number.
# time.sleep(5)
# phone = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
# if phone.text == "":
#     phone.send_keys(PHONE)

# #Submit the application
# submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
# submit_button.click()