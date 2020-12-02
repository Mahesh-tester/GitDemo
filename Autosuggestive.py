import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:\\Users\\Raghu\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)

element=driver.find_elements_by_xpath("//li[@class='ui-menu-item']/a")
for ele in element:
    if ele.text== 'India':
        ele.click()

