from selenium import webdriver

driver=webdriver.Chrome("C:\\Users\\Raghu\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/windows")

parent=driver.current_window_handle
driver.find_element_by_link_text("Click Here").click()

handles=driver.window_handles


for handle in handles:
    if handle not in parent:
        driver.switch_to.window(handle)
        print(handle)

