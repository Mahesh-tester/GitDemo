import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

list=[]
list2=[]
driver=webdriver.Chrome("C:\\Users\\Raghu\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(2)
buttons=driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

vegies=driver.find_elements_by_css_selector("p.product-name")
for veg in vegies:
    list2.append(veg.text)
print(list2)
wait=WebDriverWait(driver,6)


total=driver.find_element_by_css_selector("span.totAmt").text

driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))

afterdiscount=driver.find_element_by_css_selector("span.discountAmt").text

assert int(total) > float(afterdiscount)

amounts=driver.find_elements_by_xpath("//td[5]/p")

sum=0
for amount in amounts:
    sum=sum+int(amount.text)
print(sum)

assert int(total) == int(sum)