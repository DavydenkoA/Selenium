'''
В вашем пути к завершению задачи на курсе внезапно возникла преграда: элемент, который вам необходимо кликнуть,
оказался перекрыт другим элементом. Вы столкнулись с ошибкой,

selenium.common.exceptions.ElementClickInterceptedException: Message: element click
intercepted: Element <button class="btn" onclick="clicks()">...</button> is not clickable at point (135, 179).
Other element would receive the click: <div class="block2"></div>
и теперь вашей задачей является обойти это препятствие. Необходимо научиться получать фокус нужного элемента,
даже если он перекрыт другими объектами на странице.

Selenium: Ваш основной инструмент для взаимодействия с веб-страницей:
http://parsinger.ru/scroll/4/index.html
Этапы миссии:

Идентификация Элемента: Первым делом необходимо найти элемент, с которым вы хотите взаимодействовать.
# Пример поиска элемента по ID
browser.find_element(By.ID, 'btn')
Получение Фокуса: Воспользуйтесь методом scrollIntoView для того, чтобы прокрутить страницу так, чтобы нужный
элемент оказался в видимой области.
# Пример получения фокуса элемента
element = browser.find_element(By.CLASS_NAME, 'btn')
browser.execute_script("return arguments[0].scrollIntoView(true);", element)
Клик по Элементу: Теперь, когда элемент в фокусе, попробуйте снова выполнить клик.
Проверка Результата: Убедитесь, что ваше взаимодействие с элементом привело к желаемому результату
(в теге с  <p id="result">788544</p> появляется уникальное для каждой кнопки число).
Суммирование:  Суммируйте все полученные числа.
Завершающий этап: Вставьте полученную сумму в поле ответов на Степике.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

# скрытый режим
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--headless=new')
#with webdriver.Chrome(options=options_chrome) as browser:
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/4/index.html')
    button = browser.find_elements(By.CLASS_NAME, 'btn')
    lst = []
    for x in button:
        browser.execute_script("return arguments[0].scrollIntoView(true);", x)
        x.click()
        lst.append(int(browser.find_element(By.ID, 'result').text))
    print(sum(lst))