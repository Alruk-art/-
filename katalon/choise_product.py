# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome('c://brodriver/chromedriver')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://tutorialsninja.com/demo/index.php?route=common/home")
        driver.find_element_by_name("search").click()
        driver.find_element_by_name("search").clear()
        driver.find_element_by_name("search").send_keys("product")
        driver.find_element_by_xpath("//div[@id='search']/span/button").click()
        driver.find_element_by_xpath("//div[@id='content']/div[3]/div/div/div[2]/div[2]/button[1]").click()

        driver.find_element_by_id("input-option224").click()
        Select(driver.find_element_by_id("input-option224")).select_by_visible_text("Medium (+$12.00)")
        driver.find_element_by_id("button-cart").click()
        driver.find_element_by_xpath("//div[@id='top-links']/ul/li[4]/a").click()
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        driver.find_element_by_xpath("//*[@id='content']/form/div/table/tbody/tr/td[4]/div/input").click()
        driver.find_element_by_xpath("//*[@id='content']/form/div/table/tbody/tr/td[4]/div/input").clear()
        driver.find_element_by_xpath("//*[@id='content']/form/div/table/tbody/tr/td[4]/div/input").send_keys("2")
        driver.find_element_by_xpath("//div[@id='content']/form/div/table/tbody/tr/td[4]/div/span/button/i").click()
        driver.find_element_by_xpath("//div[@id='content']/form/div/table/tbody/tr/td[4]/div/span/button[2]/i").click()
        driver.find_element_by_link_text("Your Store").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
