'''
Поиск чисел
Добро пожаловать в удивительный мир веб-скрапинга, где информация иногда прячется в самых неожиданных местах!
Ваша задача сегодня — вычислить и собрать числа, которые могут появиться на веб-странице. Они могут быть ключами к
более сложным задачам или даже просто интересным головоломкам.
Цель
Инициализация: Откройте заданный веб-сайт "http://parsinger.ru/scroll/2/index.html" с помощью Selenium.
Обнаружение чекбоксов: На сайте будет 100 чекбоксов. Если кликнуть на чекбокс, может появится число в теге span
<span id="result1">954</span>

Вычисление: Соберите все эти числа и сложите их.
Отправка ответа: Введите сумму всех чисел, в поле ответа на Stepik.
Заметки и подсказки
Изучите структуру HTML-страницы, чтобы понять, как Selenium может найти элементы.
Будьте осторожны: числа могут появляться и исчезать, поэтому убедитесь, что вы собрали их все.
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/2/index.html')

    txt = browser.find_elements(By.XPATH, '//span')
    input_tags = browser.find_elements(By.TAG_NAME, 'input')
    lst = []
    step = 0

    for x in txt:
        input_tags[step].send_keys(Keys.DOWN)  # Отправляем клавишу "Вниз"
        browser.execute_script("return arguments[0].scrollIntoView(true);", input_tags[step])
        input_tags[step].click()
        step += 1
        if x.text != '':
            lst.append(int(x.text))
    print(sum(lst))



