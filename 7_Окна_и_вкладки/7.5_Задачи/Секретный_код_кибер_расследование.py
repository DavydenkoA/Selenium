'''
Секретный код: кибер-расследование
Внимание, будущий кибераналитик! Перед вами стоит интересная и несколько запутанная задача, связанная с поиском
секретного кода. Вы окажетесь на месте преступления с множеством улик, но лишь одна из них окажется правильной.
Будьте внимательными и удачи в расследовании!

Цель
Место преступления: Откройте указанный сайт (https://parsinger.ru/selenium/5.8/3/index.html) с помощью Selenium.

Улики на месте: На сайте вы найдете список пин-кодов. Однако среди них лишь один правильный.

Расшифровка: Для проверки каждого пин-кода используйте кнопку "Проверить". При верном пин-коде вы получите
секретный код.

Доклад о проведенной работе: Вставьте полученный секретный код в специальное поле для на степик.

Важные заметки
Проанализировав обратную связь студентов, было выявлено, что многие из них делают одну и ту же ошибку при попытке
отправить пин-код. Чтобы избежать этой ошибки, следуйте примеру ниже:

Правильный способ:

for pin in pin_codes:
    extracted_text = pin.text
    browser.send_keys(extracted_text)
Неправильный способ:

for pin in pin_codes:
    browser.send_keys(pin.text)
В мире кибербезопасности детали имеют значение. Правильное решение этой задачи покажет вам, насколько важно внимание
к деталям. Удачи в расследовании, агент!
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/3/index.html')
    button = browser.find_elements(By.CLASS_NAME, 'pin')

    for x in button:
        pin = x.text
        browser.find_element(By.TAG_NAME, 'input').click()
        prompt = browser.switch_to.alert
        prompt.send_keys(pin)
        prompt.accept()
        alrm = browser.find_element(By.ID, 'result').text
        if 'Неверный пин-код' not in alrm:
            print(alrm)