'''
Здравствуйте, искатели сокровищ во вселенной веб-страниц! На этот раз перед вами стоит задача, которая напоминает
охоту за сокровищем. Но вместо того, чтобы копать ямы или искать клады на необитаемых островах, вы будете "копать"
информацию на веб-странице. Эта задача проверит вашу способность быть настойчивыми и терпеливыми, потому что
"сокровище" появляется довольно редко.
Задачи
Прибытие на "Остров": Используйте Selenium для открытия заданного веб-сайта https://parsinger.ru/methods/1/index.html
Охота на Сокровище: В элементе с id="result" иногда появляется число — это и есть ваше сокровище. Проблема в том,
что оно появляется очень редко. Вам придется обновлять страницу множество раз, пока не увидите это число.
Клад в Руках: Как только число появится, скопируйте его и вставьте в предназначенное для этого поле ответа
на вашем курсе.
Для решения этой задачи используйте.

browser.refresh()
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

# скрытый режим
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--headless=new')
#with webdriver.Chrome(options=options_chrome) as browser:
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    code = browser.find_element(By.ID, 'result').text
    while code == 'Refresh Page':
        browser.refresh()
        code = browser.find_element(By.ID, 'result').text
        if code != 'refresh page':
            print(code)
