from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import csv
import logging

#Load driver for Chrome
driver = webdriver.Chrome(executable_path = os.path.abspath('test_suites/resources/webdriver/chromedriver.exe'))

def Add_file_to_be_called():
  print(time.strftime("%H:%M:%S") + " this is a fuction from a seperate file")

  
def Login():
  try:
        csv_credentials = csv.reader(credential_file_positive)
        for LoginCredential in csv_credentials:

            logging.info(LoginCredential[0])
            try:
                loginUser = driver.find_element_by_xpath('//input[@id="UserName"]')
            except:
                logging.info(sys.exc_info()[0])

            logging.info(loginUser)
            loginUser.send_keys(LoginCredential[0])

            logging.info(LoginCredential[1])
            loginPass = driver.find_element_by_xpath('//input[@id="Password"]')
            loginPass.send_keys(LoginCredential[1])
            
            
            loginButtonClick = driver.find_element_by_xpath('//*[@id="LogonButton"]/table/tbody/tr/td/input')
            loginButtonClick.click()

        credential_file_positive.close()
        logging.info('Credentials inputted')
  except:
        logError(loginPositive)

  
