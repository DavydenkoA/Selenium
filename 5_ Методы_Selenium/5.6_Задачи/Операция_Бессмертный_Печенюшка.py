'''
Ваша задача как кибердетектива — найти "Бессмертный Печенюшка" среди лабиринта из 42 разных ссылок. Этот мифический
печенюшка не прост; он обладает самым долгим сроком жизни среди всех остальных на этих страницах. Ваши средства —
мощные инструменты языка программирования, которые не оставят ему шанса скрыться от нас. Ваш ход, детектив.

Этапы миссии:

Запуск: Откройте основной сайт 'https://parsinger.ru/methods/5/index.html' с помощью Selenium. С этой точки начнётся
ваша экспедиция в поисках "Бессмертного Печенюшка".

Следование за линками: На основной странице будет 42 ссылки. Открывайте каждую из них, чтобы исследовать и выяснить,
какой из cookies имеет самый долгий срок жизни.

Вычисление жизнеспособности: Для каждой открытой страницы анализируйте срок жизни её cookie ['expiry'].
Сохраняйте эти данные для последующего сравнения.

Коронация Бессмертного: После проверки всех 42 страниц определите, на какой из них находится cookie с самым долгим
сроком жизни. С этой страницы извлеките число которое лежит в  теге <p id="result">INT</p>.

Завершающий этап: Вставьте полученное число в специальное поле для степик. Поздравляем, вы нашли
"Бессмертного Печенюшка" и преуспели в этой миссии!
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

# скрытый режим
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--headless=new')
#with webdriver.Chrome(options=options_chrome) as browser:
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/5/index.html')
    l_href = [item.get_attribute('href') for item in browser.find_elements(By.TAG_NAME, 'a')]
    expiry = 0
    result = 0
    for link in l_href:
        browser.get(link)
        cookies = browser.get_cookies()
        for key in cookies:
            if key['expiry'] > expiry:
                result = browser.find_element(By.ID, 'result').text
                expiry = key['expiry']
    print(result)

