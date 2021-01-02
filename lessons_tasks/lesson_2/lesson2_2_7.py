# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')
try:
    browser.find_element_by_name('firstname').send_keys('name')
    browser.find_element_by_name('lastname').send_keys('lastName')
    browser.find_element_by_name('email').send_keys('my@email.py')
    browser.find_element_by_name('file').send_keys(
        os.path.join(os.path.abspath(os.getcwd()),
                     'resources/simple_file.txt'))
    btn = browser.find_element_by_xpath('//button[text()="Submit"]').click()
finally:
    time.sleep(15)
    browser.quit()
