import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:\\Users\\Raghu\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_id("name").send_keys("Hello")

driver.find_element_by_id("alertbtn").click()
alert=driver.switch_to.alert
print(alert.text)
time.sleep(3)
alert.accept()