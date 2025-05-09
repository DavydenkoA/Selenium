import time
from selenium import webdriver

# Задаем опции для Chrome
options_chrome = webdriver.ChromeOptions()
# Указываем путь к профилю пользователя
options_chrome.add_argument('user-data-dir=C:\\Users\\daf80\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1')

# Инициализируем драйвер с указанными опциями
with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)  # Открываем страницу
    time.sleep(10)  # Даем время на загрузку страницы

'''
Если все сделано правильно, то у вас запустится окно браузера с вашими параметрами, историей, закладками.

Если при запуске этого кода возникает ошибка, сообщающая, что директория данных пользователя уже используется 
(например, "invalid argument: user data directory is already in use, please specify a unique value for"), 
это означает, что ваш основной браузер Chrome в данный момент использует этот профиль. Вам нужно закрыть основной 
браузер и повторить попытку.
Если вам нужно одновременно работать с основным окном браузера и сессией Selenium, скопируйте папку User Data в 
другое место и укажите путь к этой копии в user-data-dir, как это делалось выше.'''