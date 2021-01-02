# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')

try:
    num_1 = int(browser.find_element_by_css_selector('#num1').text)
    num_2 = int(browser.find_element_by_css_selector('#num2').text)
    print(num_1)
    print(num_2)
    res = num_1 + num_2
    print(res)

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_visible_text(f'{res}')
    browser.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(15)
    browser.quit()

    # select = Select(browser.find_element_by_css_selector('#dropdown'))
    # select.select_by_visible_text(res)
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(5)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
