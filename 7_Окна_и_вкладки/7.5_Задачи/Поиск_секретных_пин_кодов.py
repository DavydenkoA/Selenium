'''
Поиск секретных пин-кодов
В мире программирования часто встречаются тайны и загадки, которые ждут своего решения. Сегодня вы столкнетесь с
одной из таких тайн. Представьте себя в роли брутфорса, который ищет секретный пин-код среди множества ложных следов.

Цель
Доступ к месту преступления: Используйте Selenium, чтобы получить доступ к веб-сайту
(https://parsinger.ru/selenium/5.8/2/index.html), где спрятаны улики.

Внимательное расследование: На сайте находится 100 кнопок. Каждая из них при нажатии активирует всплывающее alert
окно с пин-кодом.

Расшифровка: Под кнопками расположено текстовое поле, которое проверяет пин-коды. Ваша задача — ввести пин-код и
проверить его. Если пин-код верный, вы получите секретный код.

Завершение задачи: Вставьте полученный секретный код в специальное поле для ответа на степик.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/2/index.html')
    button = browser.find_elements(By.CLASS_NAME, 'buttons')

    for x in button:
        x.click()
        pin = browser.switch_to.alert.text
        cnfrm = browser.switch_to.alert
        cnfrm.accept()
        browser.find_element(By.ID, 'input').send_keys(pin)
        browser.find_element(By.XPATH, '//input[@value="Проверить"]').click()
        alrm = browser.find_element(By.ID, 'result').text
        if 'Неверный пин-код' not in alrm:
            print(alrm)
