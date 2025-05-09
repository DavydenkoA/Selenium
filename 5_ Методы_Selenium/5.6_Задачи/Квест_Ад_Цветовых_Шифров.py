'''
Приветствую, фанаты автоматизации и парсинга! Сегодня у нас не просто задание, а настоящий квест. Перед вами
полотно веб-страницы, и ваша задача — расшифровать его, как настоящие криптографы цветов. Используя Selenium,
вам нужно будет пройти через лабиринт элементов, собрать все цветовые коды и применить их для различных
задач на странице.

Что вас ждёт на странице.
50 уникальных контейнеров (div), каждый с собственным случайным фоновым HEX цветом.
В каждом блоке присутствует выпадающий список с множеством HEX цветов.
Кнопки с разными цветами и уникальным атрибутом data-hex=.
Чек-боксы и текстовые поля, которые также хотят участвовать в этой великой красочной головоломке.

Что нужно сделать
Загрузка Страницы: Откройте страницу 'https://parsinger.ru/selenium/5.5/5/1.html' с помощью Selenium.

Используйте эту страницу 'https://parsinger.ru/selenium/5.5/5/1.html' с двумя элементами для тренировки.

Коды Цветов: Получите цвет в формате HEX из каждого элемента <span>.

Выбор в Списке: В выпадающем списке в каждом контейнере найдите и выберите тот же HEX цвет что и
у родительского контейнера.

Кнопочная Магия: Найдите и нажмите на кнопку, у которой атрибут data-hex совпадает с HEX
цветом родительского контейнера.

Чек-Бокс Челлендж: Поставьте галочку в чек-боксе на странице.

Текстовое Поле: Вставьте в текстовое поле тот же HEX-цвет, который имеет фон родительского контейнера.

Подтверждение: Нажмите на кнопку "Проверить": если вставлен корректный HEX, то на кнопке появится "ОК".

Повторение: Повторите все эти шаги для каждого найденного на странице контейнера.

Финальный Шаг: После выполнения всех действий, нажмите на кнопку "Проверить все элементы", кнопка расположена
в самом низу, появится alert если все условия соблюдены.

Секретный Код: Из алерт-окна получите числовой код и вставьте его в поле ответа степик.

Примечания
Внимательно следите за атрибутами элементов, чтобы правильно их выбрать.
Код должен быть универсальным и работать со всеми найденными на странице элементами.
'''
import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# скрытый режим
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--headless=new')
#with webdriver.Chrome(options=options_chrome) as browser:
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/5/1.html')
    main_cont = browser.find_elements(By.XPATH, '//div[@id="main-container"]/div')
    for hex_color in main_cont:
        color = hex_color.find_element(By.TAG_NAME, 'span').text
        select = Select(hex_color.find_element(By.TAG_NAME, 'select'))
        select.select_by_value(color)
        hex_color.find_element(By.XPATH, f'.//button[@data-hex="{color}"]').click()
        hex_color.find_element(By.XPATH, './/input[@type="checkbox"]').click()
        hex_color.find_element(By.XPATH, './/input[@type="text"]').send_keys(color)
        hex_color.find_element(By.XPATH, './/button[text()="Проверить"]').click()
    browser.find_element(By.XPATH, '//button[text()="Проверить все элементы"]').click()
    print(browser.switch_to.alert.text)
