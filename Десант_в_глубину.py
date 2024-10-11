'''
Десант в глубину: Поиск сокровищ среди скрытых элементов
Добро пожаловать в мир загадочных данных, где информация не так просто дается в руки исследователей. В этой задаче,
схожей с пещеролазанием в глубины веба, вам предстоит использовать Selenium и дополнительный инструментарий
ActionChains для автоматизации глубокого скроллинга. Цель? Собрать все числа из недр этой цифровой пещеры и
скомпоновать их в одну общую сумму.

Задача
Инициализация: Откройте заданный веб-сайт (http://parsinger.ru/infiniti_scroll_2/) с помощью Selenium.

Техника скроллинга: Сайт содержит список из 100 элементов, которые появляются только при скроллинге.
Стандартные элементы типа чекбоксов или другие элементы для "зацепления" тут отсутствуют.

Навигация: Прокрутите страницу до самого низа, используя ActionChains.

Сбор информации: Извлеките все числовые значения из появившихся элементов и сложите их.

Отправка результата: Вставьте полученную сумму в соответствующее поле для ответа на степик.
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/infiniti_scroll_2/')

    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')

    for x in range(10):
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()

    summa = browser.find_elements(By.XPATH, '//p')
    summa_lst = []

    for g in summa:
        if (g.text).isdigit():
            summa_lst.append(int(g.text))
    print(sum(summa_lst))


    #print(sum((number.text) for number in browser.find_elements(By.XPATH, '//p') if number.text))