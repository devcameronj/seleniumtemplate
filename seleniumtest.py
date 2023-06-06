# import time
# import getpass
# import sys
# import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



# Specify the path to the ChromeDriver executable
driver_path = 'Lib\site-packages\chromedriver'

# Create a Service object
service = Service(driver_path)

# Create a WebDriver instance and pass the Service object
driver = webdriver.Chrome(service=service)

# Request the page to automate
driver.get('https://www.jyothicameron.dev')

# # Grab the element you want to interact with 
# element = driver.find_element_by_id('input_id')

# # Send data like the following: 
# element.send_keys('username') # sends txt
# element.send_keys('password') # sens text
# element.send_keys(Keys.ENTER)  # Simulate pressing the Enter key
# element.send_keys(Keys.TAB)  # Simulate pressing the Tab key
# element.send_keys(Keys.CONTROL + 'a')  # Simulate pressing Ctrl+A
# element.send_keys(Keys.CONTROL + 'c')  # Simulate pressing Ctrl+C

# time.sleep(10)

input('Press Enter to stop script...\n')
driver.quit()
