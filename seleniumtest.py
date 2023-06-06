# import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# element.send_keys(Keys.ENTER)  # Simulate pressing the Enter key
# element.send_keys(Keys.TAB)  # Simulate pressing the Tab key
# element.send_keys(Keys.CONTROL + 'a')  # Simulate pressing Ctrl+A
# element.send_keys(Keys.CONTROL + 'c')  # Simulate pressing Ctrl+C

# Specify the path to the ChromeDriver executable
driver_path = 'Lib\site-packages\chromedriver'

# Create a Service object
service = Service(driver_path)

# Create a WebDriver instance and pass the Service object
driver = webdriver.Chrome(service=service)


driver.get('https://www.jyothicameron.dev')
# element = driver.find_element_by_id('input_id')
# element.send_keys('username')
# element.send_keys('password')


# time.sleep(10)

input('Press Enter to stop script...\n')
driver.quit()
