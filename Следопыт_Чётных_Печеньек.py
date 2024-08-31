'''
Вы — киберархеолог. Ваша миссия — раскопать древние и загадочные "печеньки" (cookies) на таинственном веб-сайте.
Но не просто так. Ваша задача собрать только особые печеньки — те, что имеют чётные числа после символа "_".
Суммируйте числовые значения этих "печенек" и используйте их как ключ к следующему уровню этого цифрового лабиринта.
Этапы миссии:

Запустите ваш кибер-копатель и отправьтесь на заданный сайт:
https://parsinger.ru/methods/3/index.html

Особая задача сбора: Соберите только те "печеньки", значения которых имеют чётные числа после символа "_". Например,
если cookie имеет имя "session_12", число "12" является чётным, и это именно то, что вам нужно.

Анализ и суммирование: Суммируйте числовые значения этих особых "печенек". Это сумма будет вашим ключом.

Ввод ответа: После расшифровки вставьте ваш ключ в специальное поле для ответов на степик. Успех здесь означает ваш
переход на следующий уровень задания.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

# скрытый режим
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--headless=new')
#with webdriver.Chrome(options=options_chrome) as browser:
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    lst = []
    for x in cookies:
        if int(x.get('name')[14:]) % 2 == 0:
            lst.append(int(x.get('value')))
    print(sum(lst))