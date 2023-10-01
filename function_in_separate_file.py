from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import csv
import sys

TimeTaken = "0"

timestamp = time.strftime("%Y%m%dT%H%M%S")
fmt = "%Y-%m-%dT%H:%M:%S.%f%z"
datefmt = "%d/%m/%Y"
filetimestampfmt = "%Y%m%dT%H%M%S"
now_utc = datetime.now(timezone('UTC'))
now_pacific = now_utc.astimezone(timezone('US/Pacific'))
now_AEST = now_pacific.astimezone(timezone('Australia/Melbourne'))
time_AEST = now_AEST.strftime(fmt)
filetime_AEST = now_AEST.strftime(filetimestampfmt)



'''
Configuration & Prepwork for modules
'''
# Logging
# Check if log, and screenshots folder is present. If not, make them.
if not os.path.exists('log'):
    os.mkdir('log')
if not os.path.exists('SumoLogs'):
    os.mkdir('SumoLogs')    
#if not os.path.exists('log/screenshots'):
#    os.mkdir('log/screenshots')
# Logging Configuration
logging.basicConfig(
                        filename=os.path.abspath('log/DJ_RESULTS-' + filetime_AEST +'.log'),
                        level=logging.INFO,
                        format='%(levelname)s - %(asctime)s - %(message)s',
                        filemode='a',
                        datefmt='%d-%b-%y %H:%M:%S',
                    )




startUrl = sys.argv[1]
MonitoringStatus = sys.argv[2]
Environ = sys.argv[3]


def Add_file_to_be_called():
  print(time.strftime("%H:%M:%S") + " this is a fuction from a seperate file")

  
def Login():

  #update login function
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

  
        credentials.close()
  except:
        logging.info('Failed to load login details')



