from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = 'PATH OF DRIVER'
driver = webdriver.Chrome(PATH)

driver.get("SITE YOU WANT TO SCRAP")

search = driver.find_element_by_name("s")
search.send_keys("Test")
search.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()
