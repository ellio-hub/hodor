#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get('http://158.69.76.135/level0.php')
input_v = driver.find_element_by_name("id")
input_v.send_keys("1421")
input_v.send_keys(Keys.RETURN)
for i in range(1024):
    driver.refresh()
driver.quit()
