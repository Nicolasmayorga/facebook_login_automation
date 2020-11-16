#Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Other
import time

print("test case started")
#open Google Chrome browser
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.maximize_window()
driver.delete_all_cookies()


#navigate to the url
driver.get("https://www.facebook.com")
driver.find_element_by_xpath('//*[@id="email"]').send_keys("nmayorgav@gmail.com")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys("8C@racteres")
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').send_keys(Keys.ENTER)
time.sleep(1)
#close the browser
driver.close()
print("facebook login has been successfully completed")