from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import time


def Add_file_to_be_called():
  print(time.strftime("%H:%M:%S") + " this is a fuction from a seperate file")
