'''
Добро пожаловать в лабораторию мастера заполнения форм! Перед вами стоит непростая задача: вскрыть виртуальный сейф,
заполнить поля аутентификации и взять "ключ", который появляется на экране. И конечно же, это нужно сделать всё в
течение трёх секунд. Научимся пользоваться инструментами хакера в лучших традициях Hollywood, но в нашем случае всё
будет законно и для образовательных целей!

Основные Этапы:
Точка Входа: Откройте заданный веб-сайт с помощью Selenium.
Сканирование: Используйте метод .find_elements() для поиска всех доступных полей для ввода на странице.
Ввод данных: В цикле, переберите все найденные поля и заполните их с помощью метода .send_keys("Текст").
Инициация: Найдите кнопку на странице и нажмите на неё.
Результат: Скопируйте текст, который появится на экране рядом с кнопкой, если вы уложились в трёх секундный интервал.
Фиксация: Запишите результат в отдельную переменную или вставьте ответ в поле ответа степик.
Код, чтобы освежить память.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_form = browser.find_element(By.CLASS_NAME, 'form').send_keys('Text')
    time.sleep(5)
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_form = browser.find_elements(By.CLASS_NAME, 'form')#.send_keys('Text')
    for i in input_form:
        i.send_keys('Текст')
    browser.find_element(By.ID, 'btn').click()
    result = browser.find_element(By.ID, 'result').text
    print(result)
    #print(input_form[0].text)
    time.sleep(5)