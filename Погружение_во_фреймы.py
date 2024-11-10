'''
Вы — кибердетектив, и перед вами стоит необычная загадка. В цифровом мире скрыт ключ к таинственному сейфу. Этот ключ
спрятан в одной из цифровых комнат — iframe'ах. Ваша задача — проявить свои навыки и найти этот ключ. Но будьте
осторожны, не каждая комната даст вам ответ!

Цель
Погружение в кибермир: Используя Selenium, перейдите на указанный сайт(https://parsinger.ru/selenium/5.8/5/index.html).

Поиск зеркальных комнат: На сайте вы обнаружите 9 iframe. В каждом из них скрыта кнопка.

Сбор информации: Нажмите на кнопку в каждом iframe, чтобы получить число. Но помните, с вероятностью 1/9 это число
окажется тем самым ключом к сейфу.

Открытие тайны: Вставьте полученное число в поле для проверки. Если удача на вашей стороне, то это число откроет
перед вами секретный код в alert.

Вставьте полученный код из alert в поле ответа степик.

Подсказка
# Пареключится на iframe
driver.switch_to.frame(iframe)

# Вернутся к базовому контенту страницы
driver.switch_to.default_content()
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/5/index.html')
    frame = browser.find_elements(By.TAG_NAME, 'iframe')

    for x in frame:
        browser.switch_to.frame(x.get_attribute('id'))
        browser.find_element(By.TAG_NAME, 'button').click()
        dig = browser.find_element(By.ID, 'numberDisplay').text
        browser.switch_to.default_content()
        browser.find_element(By.ID, 'guessInput').clear()
        browser.find_element(By.ID, 'guessInput').send_keys(dig)
        browser.find_element(By.ID, 'checkBtn').click()
        try:
            print(browser.switch_to.alert.text)
        except:
            pass

#FD79-32DJ-79XB-124S-P3DX-2456-DFB-DSA9