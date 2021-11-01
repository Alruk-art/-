#!/usr/bin/python3
# -*- encoding=utf8 -*-
"""Автоматизация с чего начать?"""
from seleniumbase import BaseCase
class AppleTestClass(BaseCase):

    def test_apple_developer_site_webdriver_instructions(self):
        self.demo_mode = True
        self.demo_sleep = 1
        self.message_duration = 2.0
        self.open('https://developer.apple.com/search/')
        title = 'Testing with WebDriver in Safari'
        self.type('[placeholder *= "developer.apple.com"]', title + "\n")
        self.click("link=%s" % title)
        self.assert_element('nav.documentation-nav')
        self.assert_element('div.nav-title [href*="/documentation/"]')
        self.assert_text(title, "h1")
        self.highlight("div.description ")
        self.highlight("h2")
        h3 = "h3:nth-of-type(%s)"
        self.assert_text("Make Sure You Have Safari’s WebDriver", h3 % "1")
        self.assert_text("Get the Correct Selenium Library Version", h3 % "2")
        self.assert_text('Configure Safari to Enable WebDriver Support',  h3 % "3")
        self.assert_text('Write a WebDriver Testing Suite', "h3:nth-of-type(4)")
        self.assert_text('Run Your Test', "h3:nth-of-type(5)")