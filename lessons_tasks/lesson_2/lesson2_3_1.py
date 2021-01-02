# -*- coding: utf-8 -*-

"""
Работа с модальными окнами
Зачастую модульные окна бывают следующих типов:
- alert
- confirm
- prompt

для взаимодействия с ними необходимо сперва на них переключиться
browser.switch_to.alert

Alert
Для того, чтобы закрыть:
alert = browser.switch_to.alert
alert.accept()

Для того, чтобы получить содежимое алерта
alert = browser.switch_to.alert
alert_text = alert.text

Confirm
confirm = browser.switch_to.alert
confirm.accept() - подтвердить
confirm.dismiss() - отказ

Prompt
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()

Работа с новыми окнами
Открыть новое окно можно следующим образом
browser.switch_to.window(window_name)

получить список всех открытых окон можно при помощи
new_window = browser.window_handles[1]
window_handles - возвращает массив имён всех окон браузера
"""
