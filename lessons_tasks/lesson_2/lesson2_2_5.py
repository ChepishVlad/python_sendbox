# -*- coding: utf-8 -*-
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/execute_script.html')
    y = calc(browser.find_element_by_css_selector('#input_value').text)

    input_ = browser.find_element_by_css_selector('#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_)
    input_.send_keys(y)

    check = browser.find_element_by_css_selector('#robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", check)
    check.click()

    radio = browser.find_element_by_css_selector('#robotsRule').click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    btn = browser.find_element_by_xpath('//button[text()="Submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()
finally:
    time.sleep(15)
    browser.quit()
