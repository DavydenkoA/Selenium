'''
Представьте себя хакером-белой шляпы, вооруженным навыками веб-скрапинга и автоматизации. Ваша миссия, если вы её
примете, — раскрывать секреты веб-сайтов, чтобы обеспечить их безопасность и устойчивость. Не просто кодером, вы —
кибердетектив. И вот ваше следующее задание:

Цель: Получить все секретные "cookies" с заданного веб-сайта и суммировать их числовые значения. Эти "cookies" могут
хранить важную информацию, например, ключи для доступа к секретным данным. Ваши навыки веб-парсинга здесь будут более
чем полезны.
Этапы миссии:
Вооружитесь браузером и пусть ваш код проникнет на сайт 'https://parsinger.ru/methods/3/index.html'.
Поиск секретных cookies: Найдите все скрытые secret_cookie_, которые могут содержать важную информацию.

Дешифровка и анализ: Суммируйте числовые значения всех secret_cookie_. Это может быть частью шифра или ключом к
следующему уровню.
Ввод ответа: Вставьте полученную сумму в поле ответа степик. Это ваш ключ к успешному завершению миссии.
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
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    secret_cookies = []
    for secret in cookies:
        secret_cookies.append(int(secret.get('value')))
    print(sum(secret_cookies))