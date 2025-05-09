'''
Цель: Определить уникальное сочетание размеров из двух списков, которое активирует скрытый контент на странице.

Инициализация: Используя Selenium, откройте заданный сайт (http://parsinger.ru/window_size/2/index.html).
Анализ списков размеров: У вас есть два списка размеров – window_size_x и window_size_y.
Тестирование: Примените каждое сочетание размеров из этих списков к окну вашего браузера.
Поиск результата: После каждой установки размера проверяйте содержимое элемента с идентификатором
id="result" на странице.
Извлечение данных: Как только найдете уникальное сочетание, при котором на странице появляется число,
скопируйте его и вставьте в поле для ответа.
Подсказка: Размеры рамок и панелей браузера могут влиять на видимую область страницы. Убедитесь, что учли этот
фактор при настройке размера окна.
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/window_size/2/index.html')
    time.sleep(1)

    window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

    for x in window_size_x:
        for y in window_size_y:
            browser.set_window_size(x, y)
            x_in = browser.find_element(By.ID, 'width').text
            y_in = browser.find_element(By.ID, 'height').text
            x_real = browser.get_window_size().get('width')
            y_real = browser.get_window_size().get('height')
            x_delta = x_real - int(x_in[3:])
            y_delta = y_real - int(y_in[3:])

            browser.set_window_size(x + 13, y + 145)

            #print(x_in[3:], y_in[3:], ' ', x_real, y_real, ' ', x_delta, y_delta)

            alrm = browser.find_element(By.ID, 'result').text
            #time.sleep(1)
            if alrm:
                print(alrm)

'''
Код рабочий, но надо доделать, задание еще не выполнено
'''

