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
driver.find_element(By.XPATH, "//h3[text()='Wipro – Transform Digitally with Our Technology and IT ...']").click()
driver.find_element(By.XPATH, "//button[@title='Accept']").send_keys("\n")
WiproTitle = driver.title
Expected_title = "Wipro – Transform Digitally with Our Technology and IT Consulting Services"
if WiproTitle == Expected_title:
    print("Page is Up")
else:
    print("Page is down")

time.sleep(5)
print("Good night")