
#python -m pytest -v --driver Chrome --driver-path c://brodriver/chromedriver
#C:\pythonProjectNat\QANat\open_google.py

from selenium import webdriver
import time
wdr = webdriver.Chrome('c://brodriver/chromedriver')

wdr.get('https://www.google.ru/')
#search_box = wdr.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_box = wdr.find_element_by_xpath("(//input[@name='q'])")
search_box.send_keys('atom')

search_button = wdr.find_element_by_xpath("(//input[@type='submit'])")
#search_button = wdr.find_element_by_xpath("(//input[@name='btnK'])")
#search_button = wdr.find_element_by_class_name("gNO89b")
search_button.click()


# тестируем ютуб
wdr.get('https://www.youtube.ru/')
time.sleep(5)
search_box = wdr.find_element_by_xpath('//ytd-searchbox/form/div/div[1]/input')
search_box.send_keys('atom')

search_button = wdr.find_element_by_xpath('//*[@id="search-icon-legacy"]')
search_button.click()
time.sleep(3)
wdr.quit()

