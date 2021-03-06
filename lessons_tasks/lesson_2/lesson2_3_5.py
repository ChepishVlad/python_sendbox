# -*- coding: utf-8 -*-
import time
from math import log, sin
from selenium import webdriver


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get('http://suninjuly.github.io/redirect_accept.html')

try:
    browser.find_element_by_class_name('btn-primary').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    y = calc(browser.find_element_by_css_selector('#input_value').text)
    browser.find_element_by_css_selector('#answer').send_keys(y)
    browser.find_element_by_xpath('//button[text()="Submit"]').click()
finally:
    time.sleep(15)
    browser.quit()
