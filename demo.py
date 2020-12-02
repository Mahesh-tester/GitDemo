
import time

from selenium import webdriver
class Test:

    def one(self):

        driver=webdriver.Chrome("C:\\Users\\Raghu\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(5)

        driver.get("https://www.makemytrip.com/")

        driver.find_element_by_xpath("//label[@for='fromCity']").click()

        # Clicking on From City
        driver.find_element_by_xpath("//input[@placeholder='From']").send_keys("Del")
        time.sleep(3)


        cities = driver.find_elements_by_css_selector("p[class*='blackText']")
        for city in cities:
            if city.text == "Kerala, India":
                city.click()
                break

        driver.find_element_by_xpath("//p[text()='Goa, India']").click()

        element=driver.find_element_by_css_selector("div[class*='dates'] label[for='departure']")
        driver.execute_script("arguments[0].click();", element)

        calmonth=driver.find_element_by_xpath("//div[@class='DayPicker-Months']/div[position()=1]")

        allvalidates=calmonth.find_elements_by_tag_name("p")

        for date in allvalidates:
            if date.text=='29':
                date.click()
                break

        time.sleep(10)


tt=Test()
tt.one()


