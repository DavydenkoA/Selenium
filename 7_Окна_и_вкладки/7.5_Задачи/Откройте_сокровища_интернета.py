'''
Цель: Найти скрытые коды на списках сайтов, обработать их и получить конечный результат.

Сюжет: В глубинах интернета расположены сайты, каждый из которых хранит свой уникальный код. Этот код – лишь часть
большой головоломки, которую вам предстоит разгадать.

Шаги к решению:

Подготовка: Загрузите список сайтов, на которых скрыты коды.
Открытие вкладок: Используя Selenium, откройте каждый сайт в отдельной вкладке.
Поиск кодов: Пройдитесь по всем вкладкам и найдите чекбокс. Нажмите на него, чтобы получить код.
Обработка данных: Для каждого полученного кода найдите его квадратный корень.
Суммирование: Сложите все полученные корни.
Финальное преобразование: Округлите конечную сумму до 9 знаков после запятой.
Результат: Вставьте полученное значение в поле для ответа.
Подсказки:

Верный ответ имеет вид 000000.000000000. Используйте функцию round().
Не ищите лёгких путей! Освоение работы с вкладками – это ключевой навык веб-автоматизации.
'''
import time # применяю для того чтобы смотреть как отрабатывает код
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html',
         'http://parsinger.ru/blank/1/6.html',]
with webdriver.Chrome() as browser:
    summa_sqrt = []
    for x in sites:
        browser.execute_script(f"window.open('{x}');")
        time.sleep(1)
    for y in browser.window_handles[1:]:
        browser.switch_to.window(y)
        browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
        code = browser.find_element(By.ID, 'result').text
        summa_sqrt.append(math.sqrt(int(code)))
        time.sleep(1)
    print(round(sum(summa_sqrt), 9))