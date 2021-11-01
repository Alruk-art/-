import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Testselenium(unittest.TestCase):

    def test_add_to_bascet(self) -> None:
        """добавление в корзину """

        wdr = webdriver.Chrome(
            executable_path='C://brodriver/chromedriver'
        )
        wdr.get("http://www.tutorialsninja.com/demo/")

        search_field = wdr.find_element_by_name("search")
        search_field.send_keys("product")
        search_button=wdr.find_element_by_xpath('//*[@id="search"]/span/button')
        search_button.click()
        #search_field.send_keys(Keys.RETURN)
        #wdr.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wdr.execute_script("window.scrollTo(0, 450)") # на сколько пикселей вниз
        pass
        wdr.find_element_by_xpath('//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]').click()
        #add_to_cart.click()

        #select_size = wdr.find_element_by_xpath('//*[@id="input-option224"]')
        #select_size.click()
        time.sleep(1)
        select_mod = wdr.find_element_by_xpath('//*[@id="input-option224"]/option[2]')
        select_mod.click()

        add_to_cart_2 = wdr.find_element_by_xpath('//*[@id="button-cart"]')
        add_to_cart_2.click()

        shopping_cart=wdr.find_element_by_xpath('//*[@id="top-links"]/ul/li[4]/a')
        shopping_cart.click()

        quantity = wdr.find_element_by_xpath('//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/input')
        quantity.clear()
        quantity.send_keys(2)

        refresh=wdr.find_element_by_xpath('//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[1]')
        refresh.click()


        self.assertTrue('Product 8' in wdr.page_source)

    def test_delete_from_bascet(self):
        """Удаление из корзины (пример)"""
        self.assertTrue(True)

    def test_error_add(self):
        wdr = webdriver.Chrome(
            executable_path='C://brodriver/chromedriver'
        )
        self.assertTrue('Product 9' in wdr.page_source)



        time.sleep(10)
        wdr.close()