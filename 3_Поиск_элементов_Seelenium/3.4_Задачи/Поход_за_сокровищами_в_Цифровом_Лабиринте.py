'''
Привет, юные искатели данных и загадок! Перед вами лежит миссия, которая проверит ваше умение внимательно
"читать" веб-страницы и извлекать из них нужную информацию. На таинственной странице скрыты фрагменты артефакта —
всего их 100. Они зашифрованы и размещены во вторых абзацах каждого из 200 блоков текста. Ваша задача — собрать их и
воссоздать артефакт.

Задачи
Вход в Цифровой Лабиринт: Используйте Selenium для открытия указанного веб-сайта.
Извлечение Фрагментов: Найдите и извлеките данные из каждого второго тега <p> на странице.
Воссоздание Артефакта: Просуммируйте все числовые значения, полученные из этих тегов.
Ключ к Загадке: Запишите полученную сумму в предназначенное для этого поле или выведите на экран.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    data = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
    lst = []
    for x in data:
        lst.append(int(x.text))
    print(sum(lst))