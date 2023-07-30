import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="D:/Eclipse/DriverExtensions/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.google.com")
search = driver.find_element(By.XPATH, "//textarea[@name='q']")
search.send_keys("wipro")
search.send_keys("\n")

time.sleep(5)
print("Good night")