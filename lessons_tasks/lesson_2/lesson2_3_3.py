# -*- coding: utf-8 -*-
import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
try:
    browser.get('http://suninjuly.github.io/alert_accept.html')
    browser.find_element_by_class_name('btn-primary').click()
    confirm = browser.switch_to.alert
    confirm.accept()

    y = calc(browser.find_element_by_css_selector('#input_value').text)
    browser.find_element_by_css_selector('#answer').send_keys(y)
    browser.find_element_by_xpath('//button[text()="Submit"]').click()

finally:
    time.sleep(15)
    browser.quit()
