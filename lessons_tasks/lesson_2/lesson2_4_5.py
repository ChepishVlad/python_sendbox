# -*- coding: utf-8 -*-
import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get(' http://suninjuly.github.io/cats.html')

try:
    browser.find_element_by_id("button")
finally:
    time.sleep(15)
    browser.quit()
