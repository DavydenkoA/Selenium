'''
Добро пожаловать, кибернетические ниндзя! 🐱‍💻 Сегодня перед вами стоит задача, которую можно сравнить с поиском иглы в
стоге сена. Но не просто иглы, а золотой иглы с серийным номером, затерянной в бездонном океане информации.

🕵️‍♀️ Ваша миссия, если вы примете её, — проникнуть в лабиринт бесконечных чекбоксов, появляющихся как грибы после
дождя. Каждый чекбокс — миниатюрный замок, открывающийся только при выполнении одного условия: значение его value
должно быть чётным.

🚀 Стоит вам ошибиться, и ваша миссия провалена. Но если у вас всё получится, вас ждёт не просто поздравление в чате.
Внизу появится таинственная кнопка с классом alert_button, дарующая вам секретный код. Этот код — ключ к нашей
следующей операции, так что, ниндзя, у вас нет права на ошибку.

Задача
1. Инициализация: Откройте заданный веб-сайт (https://parsinger.ru/selenium/5.7/4/index.html) с помощью Selenium.
2. Бесконечный Скроллинг: На сайте есть блок с бесконечной подгрузкой чекбоксов. Всего 100 контейнеров и в каждом
контейнере 10 чек боксов.
3. Чётный Выбор: Устанавливайте чекбоксы только с чётным значением атрибута value.
4. Алерт-Кнопка: После установки всех чекбоксов во всех контейнерах кнопка alert с классом alert_button. Нажмите на
неё, чтобы вызвать сообщение alert , в alert и будет ключ к решению задачи.
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/5.7/4/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    action = ActionChains(browser)

    while True:
        last_child = browser.find_element(By.CSS_SELECTOR, '#main_container div:last-child')
        action.move_to_element(last_child).scroll_by_amount(0, 5000).perform()
        div_elements = browser.find_elements(By.CLASS_NAME, 'child_container')
        if len(div_elements) == 100:
            break

    for div in div_elements:
        inp_elements = div.find_elements(By.TAG_NAME, 'input')
        action.move_to_element(div).perform()
        for inp in inp_elements:
            if int(inp.get_attribute('value')) % 2 == 0:
                inp.click()

    time.sleep(1)
    browser.find_element(By.CLASS_NAME, 'alert_button').click()
    alert_text = browser.switch_to.alert.text
print(alert_text)



