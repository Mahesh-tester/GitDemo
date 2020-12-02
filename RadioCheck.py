import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:\\Users\\Raghu\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

time.sleep(2)
checkboxes=driver.find_elements_by_xpath("//fieldset//input[@type='checkbox']")

for check in checkboxes:
    if check.get_attribute("value") == 'option2':
        check.click()
        assert check.is_selected()