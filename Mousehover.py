import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome("C:\\Users\\Raghu\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,100);")

action=ActionChains(driver)
action.move_to_element(driver.find_element_by_id("mousehover")).perform()
action.move_to_element(driver.find_element_by_xpath("//a[text()='Top']")).click().perform()
