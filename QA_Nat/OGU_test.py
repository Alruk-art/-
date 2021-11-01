from selenium import webdriver
import time
import pytest

@pytest.fixture(autouse=True)
def testing():
   pytest.wdr = webdriver.Chrome('c://brodriver/chromedriver')

   yield
   pytest.wdr.quit()

def test_1():
    pytest.wdr.get('https://www.google.ru/')
    #search_box = wdr.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search_box = pytest.wdr.find_element_by_xpath("(//input[@name='q'])")
    search_box.send_keys('atom')

    search_button = pytest.wdr.find_element_by_xpath("(//input[@type='submit'])")
    #search_button = wdr.find_element_by_xpath("(//input[@name='btnK'])")
    #search_button = wdr.find_element_by_class_name("gNO89b")
    search_button.click()

def test_2():
    # тестируем ютуб
    pytest.wdr.get('https://www.youtube.ru/')
    time.sleep(5)
    search_box = pytest.wdr.find_element_by_xpath('//ytd-searchbox/form/div/div[1]/input')
    search_box.send_keys('atom')

    search_button = pytest.wdr.find_element_by_xpath('//*[@id="search-icon-legacy"]')
    search_button.click()
    time.sleep(3)

