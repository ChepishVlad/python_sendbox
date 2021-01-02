# -*- coding: utf-8 -*-
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')

x = browser.find_element_by_css_selector('#treasure').get_attribute('valuex')

y = calc(x)
browser.find_element_by_css_selector('#answer').send_keys(y)
browser.find_element_by_css_selector('#robotCheckbox').click()
browser.find_element_by_css_selector('#robotsRule').click()
browser.find_element_by_xpath('//button[text()="Submit"]').click()