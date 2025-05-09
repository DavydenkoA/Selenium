'''
Представьте себя хакером данных в виртуальном мире, где информация хранится не в обычных файлах, а в скрытых
элементах на веб-страницах. Чтобы добраться до этой информации, вам нужно использовать Selenium и скрипт Python
для автоматизации скроллинга по бесконечному списку элементов. Вам предстоит собрать все числа из этих
элементов и сложить их.
Цель
Инициализация: Используя Selenium, откройте заданный веб-сайт http://parsinger.ru/infiniti_scroll_1/
Скроллинг: На сайте имеется список из 100 элементов, который расширяется при скроллинге (infinity scroll).
Сбор данных: Скрольте по интерактивным элементам, чтобы раскрыть все 100 элементов списка. Используйте Keys.DOWN или
методы ActionChains(driver).
Агрегация: Извлеките все числовые значения из этих элементов и сложите их.
Отправка ответа: Вставьте собранную сумму чисел в предназначенное поле на сайте.
Подсказки и заметки
Помните о задержках при загрузке элементов.
Последний элемент списка имеет класс last-of-list. Используйте это для прерывания цикла скроллинга.
Внимательно изучите структуру HTML-страницы. Это поможет вам понять, как искать нужные элементы.
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')

    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')

    for x in range(10):
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()

    print(sum(int(number.text) for number in browser.find_elements(By.TAG_NAME, 'span') if number.text))

