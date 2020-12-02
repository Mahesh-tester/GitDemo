from selenium import webdriver

driver=webdriver.Chrome("C:\\Users\\Raghu\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/iframe")


driver.switch_to.frame("mce_0_ifr")

driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("Hello everyone how are you")

driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)