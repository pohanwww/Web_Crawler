from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

driver = webdriver.Firefox()

driver.get("https://www.google.com/")
time.sleep(1)
search_input = driver.find_element_by_css_selector("input.gLFyf")
search_input.send_keys("python")
time.sleep(1)
search_click = driver.find_element_by_css_selector("input.gNO89b")
search_click.click()

result = driver.find_elements_by_id("resultStats")
print(result[0].text)
driver.close()