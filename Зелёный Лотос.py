'''
Представьте себе момент, когда время замирает, и все вокруг зависает в ожидании вашего действия. Вы стоите перед
четырьмя кнопками, каждая из которых — ваш шанс изменить ход событий. Но в этой задаче важно не только нажать,
но и удерживать. Да-да, вы не ослышались.

Чтобы пройти эту задачу, вам нужно приручить каждую кнопку, удерживая её до тех пор, пока она не станет зелёной.
Значение value="N" каждой кнопки указывает на минимальное время в секундах(float()), которое необходимо выдержать.

🔮 Как только все кнопки обретут изумрудный оттенок, ваше терпение будет вознаграждено: появится сообщение в alert,
скрывающее в себе ключ к следующему испытанию. Этот ключ нужно вставить в поле ответа на Stepiк, чтобы продвинуться
дальше по курсу.

Задача
Откройте сайт (https://parsinger.ru/selenium/5.7/5/index.html) с помощью Selenium.
Найдите все четыре кнопки на странице.
Определите значение value каждой кнопки. Это время, которое необходимо удерживать кнопку.
Как только все кнопки станут зелёными, вы получите сообщение в alert. Скопируйте это сообщение.
Вставьте полученное сообщение в поле ответа на Stepik.

Подсказка:
Вам потребуется использовать методы вроде ActionChains для удержания кнопки

# Пример
actions.click_and_hold(button).pause(hold_time).release(button).perform()
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.7/5/index.html')
    buttons = browser.find_elements(By.CLASS_NAME, 'timer_button')

    for x in buttons:
        ActionChains(browser).click_and_hold(x).pause(float(x.text)).release(x).perform()
    print(browser.switch_to.alert.text)


