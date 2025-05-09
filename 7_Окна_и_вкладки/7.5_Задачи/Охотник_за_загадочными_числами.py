'''
В недрах интернета скрываются многие тайны, и одна из них ждёт вас на этом сайте. Вам предстоит взять роль
исследователя, добывающего коды из множества вкладок, каждая из которых раскрывает лишь часть большой загадки.

Шаги к решению:

Погружение: Откройте сайт (http://parsinger.ru/blank/3/index.html) с помощью Selenium.
Активация тайных порталов: Нажимая на каждую из 10 кнопок, вы активируете ворота в другую вкладку. Это ваш шанс
найти одну из частей кода.
Исследование: В каждой новой вкладке ищите в title число — ваш ключ к решению.
Сбор информации: Соберите все 10 чисел и сложите их.
Завершение миссии: Вставьте итоговую сумму в поле для ответа на исходной странице.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/3/index.html')
    button = browser.find_elements(By.CLASS_NAME, 'buttons')
    summa = []
    for x in button:
        x.click()

    for x in reversed(range(len(browser.window_handles))[1:]):
        browser.switch_to.window(browser.window_handles[x])
        dig = browser.execute_script("return document.title;")
        summa.append(int(dig))
    print(sum(summa))