import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome("C:\\Users\\Raghu\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_css_selector("a[href*='shop']").click()

products=driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
   productName=product.find_element_by_xpath("div/h4/a").text
   if productName == 'Blackberry':
       product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_css_selector("button[class*='btn-success']").click()

driver.find_element_by_id("country").send_keys("ind")
wait=WebDriverWait(driver,7)
wait.until(EC.presence_of_element_located((By.LINK_TEXT,"India")))

driver.find_element_by_link_text("India").click()
checkbox=driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']")
checkbox.click()
time.sleep(3)
print(checkbox.is_selected())

driver.find_element_by_xpath("//input[@type='submit']").click()
message=driver.find_element_by_css_selector("div[class*='alert-success']").text

assert 'Success' in message

driver.save_screenshot("finalscreenshot.png")
driver.get_screenshot_as_file("usingscreen.png")


