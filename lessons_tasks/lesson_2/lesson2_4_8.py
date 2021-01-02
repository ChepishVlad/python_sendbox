# -*- coding: utf-8 -*-
import time
from math import log, sin

from selenium import webdriver


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


browser = webdriver.Chrome()
try:
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(15)
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    browser.find_element_by_xpath("//h5[contains(text(), '100')]")
    browser.find_element_by_id('book').click()

    y = calc(browser.find_element_by_css_selector('#input_value').text)
    browser.find_element_by_css_selector('#answer').send_keys(y)
    browser.find_element_by_xpath('//button[text()="Submit"]').click()
finally:
    time.sleep(5)
    browser.quit()
