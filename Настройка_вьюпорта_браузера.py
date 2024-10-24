'''
Настройка вьюпорта браузера


Цель: Проанализировать содержимое сайта, имея строгие рамки видимой области браузера.

Шаги к решению:

Инициализация: Запустите браузер через Selenium и загрузите страницу.

Настройка размеров: Откройте окно браузера так, чтобы рабочая (видимая) область страницы точно соответствовала 555x555
пикселям. Не забудьте учесть размеры рамок и панелей браузера при расчете!

Анализ: Когда условие будет выполнено секретный ключ появится в id="result";

Действие: Извлеките содержимое данного элемента и вставьте в поле для ответа.

Подсказка: Убедитесь, что учли все элементы интерфейса браузера при настройке размера окна. Размеры рамок и панелей
могут влиять на видимую область, и их необходимо учитывать в вашем решении.
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/window_size/1/')
    x_in = browser.find_element(By.ID, 'width').text
    y_in = browser.find_element(By.ID, 'height').text
    x_out = browser.get_window_size().get('width')
    y_out = browser.get_window_size().get('height')
    x_interf = int(x_out) - int(x_in[3:])
    y_interf = int(y_out) - int(y_in[3:])
    browser.set_window_size(555 + x_interf, 555 + y_interf) #browser.set_window_size(555 + 13, 555 + 145)
    alrm = browser.find_element(By.ID, 'result').text
    print(alrm)
    time.sleep(5)