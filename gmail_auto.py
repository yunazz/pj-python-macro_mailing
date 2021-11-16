import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

user = 'yunaz42'
pw='1231234'


driver = webdriver.Chrome('./chromedriver')
url = 'https://www.naver.com/'
driver.get(url);
driver.maximize_window()

action = ActionChains(driver)

driver.find_element_by_class_name('link_login').click()

elem = driver.find_element_by_id("id")
elem.send_keys(user)
elem = driver.find_element_by_id("pw")
elem.send_keys(pw)
elem.send_keys(Keys.RETURN)


driver.quit()
