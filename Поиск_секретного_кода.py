'''
Условие задачи: "Поиск секретного кода"
В мире программирования и тестирования иногда нас ставят перед загадками и головоломками, разгадка которых может
открыть новые горизонты знаний или даже вести к сокровищам. Сегодня ваша задача — найти секретный код на веб-сайте.
Но есть подвох: код скрыт среди множества кнопок, и только одна из них может его открыть.

Задание
Запуск: Откройте указанный веб-сайт (https://parsinger.ru/selenium/5.8/1/index.html) с использованием Selenium.

Исследование: На странице размещено 100 кнопок. Отправьтесь в путешествие, кликая по каждой из них, чтобы понять,
какая из них прячет желаемый код.

Обнаружение: При активации правильной кнопки, секретный код появится в теге: <p id="result">Code</p>.

Финальный штрих: Скопируйте этот код и вставьте его в специальное поле для ответа на степик.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/1/index.html')
    button = browser.find_elements(By.CLASS_NAME, 'buttons')

    for x in button:
        x.click()
        cnfrm = browser.switch_to.alert
        cnfrm.accept()
        alrm = browser.find_element(By.ID, 'result').text
        if len(alrm) != 0:
            print(alrm)