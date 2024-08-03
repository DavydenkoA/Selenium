'''
Приветствую, будущие аналитики данных и веб-скрейперы! Перед вами стоит задача, которая требует не только знаний
в программировании, но и внимания к деталям. Вам нужно "прочитать" секретный кодекс, спрятанный на веб-странице.
Кодекс разбит на 300 фрагментов и каждый из них хранится в отдельном теге <p>. Ваша задача — собрать все эти
фрагменты воедино.

Задачи
Вход в Лабиринт: Откройте указанный веб-сайт с помощью Selenium.
Ключи к Сокровищам: Извлеките данные из каждого тега <p> на странице.
Сложение Фрагментов: Просуммируйте все числовые значения, которые вы извлекли.
Отчет о Сокровищах: Запишите сумму в отдельное поле или выведите на экран, полученное
значение вставьте в поле ответа степик.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    data_1 = browser.find_elements(By.XPATH, "//div[@class='text']/p[1]")
    data_2 = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
    data_3 = browser.find_elements(By.XPATH, "//div[@class='text']/p[3]")
    lst = []
    for x in data_1:
        lst.append(int(x.text))
    for x in data_2:
        lst.append(int(x.text))
    for x in data_3:
        lst.append(int(x.text))
    print(sum(lst))

# Более короткое решение
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/selenium/3/3.html')
#     all_nums = browser.find_elements(By.TAG_NAME, 'p')
#     num_sum = 0
#     for num in all_nums:
#         num_sum += int(num.text)
#     print(num_sum)