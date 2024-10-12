'''
Операция "Пятерка": Одновременный Глубокий Скроллинг
Приветствую вас, агенты данных! Вам предстоит выполнить задание, которое на уровень сложнее прежних. Сейчас перед вами
не просто одна "пещера" с данными, а целых пять! Пять окон на одном сайте, каждое из которых требует индивидуального
подхода. Ваша задача — проникнуть в каждое из них, добыть всю информацию и аккумулировать её в одно число.

Задача
Инициализация: Откройте заданный веб-сайт (http://parsinger.ru/infiniti_scroll_3/) с помощью Selenium.

Множественная навигация: На сайте есть 5 разных окон, в каждом из которых подгружается по 100 элементов при скроллинге.

Техника скроллинга: Для каждого окна прокрутите страницу до самого низа. Здесь можно использовать ActionChains для
эффективного скроллинга.

Сбор информации: Из каждого окна извлеките все числовые значения и сложите их. Суммируйте данные из всех окон.

Отправка результата: Вставьте полученную сумму в соответствующее поле для ответа на сайте.
'''
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/infiniti_scroll_3/')

    for q in range(5):
        div = browser.find_element(By.XPATH, f'//*[@class="scroll-container_{q + 1}"]/div')
        time.sleep(.9)

        for x in range(10):
            ActionChains(browser).move_to_element(div).scroll_by_amount(0, 500).perform()
        summa = browser.find_elements(By.XPATH, '//span')
        summa_lst = []

        for g in summa:
            if (g.text).isdigit():
                summa_lst.append(int(g.text))
    print(sum(summa_lst))
