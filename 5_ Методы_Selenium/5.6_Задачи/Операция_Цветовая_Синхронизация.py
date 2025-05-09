'''
Здравствуйте, аспиранты автоматизации! Сегодня перед вами задача, которая перенесёт нас в мир цветов, чисел и быстрых
решений. Вас ждёт настоящий квест на ловкость рук и точность кода. Сможете ли вы перенести данные так, чтобы они
заиграли новыми красками? На этот раз задание не только проверит вашу скорость, но и научит работать с изменением
стилей элементов на странице. Скорость и точность — вот ваши лучшие союзники в этой миссии!

Задачи
Исследование Территории: Откройте веб-сайт 'https://parsinger.ru/selenium/5.5/4/1.html' с помощью Selenium.
Проанализируйте поля, с которыми предстоит работать.

Миссия "Синхронизация": На странице находятся 100 текстовых полей: 50 серых и 50 синих. Ваша задача — перенести числа
из серых полей в синие.
Проверка и Контроль: Нажмите на кнопку "Проверить". Если перенос чисел прошёл успешно, поля станут зелёными.

Получение Кода: Секретный код появится только в том случае, если все поля успешно стали зелёными. Секретный код
нужно будет вставить в поле для ответа на степик.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

# скрытый режим
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--headless=new')
#with webdriver.Chrome(options=options_chrome) as browser:
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/4/1.html')
    check = browser.find_elements(By.CLASS_NAME, 'parent')
    for x in check:
        num = x.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]').text
        x.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]').clear()
        x.find_element(By.CSS_SELECTOR, 'textarea[color="blue"]').send_keys(num)
        x.find_element(By.TAG_NAME, 'button').click()
    browser.find_element(By.ID, 'checkAll').click()
    print(browser.find_element(By.ID, 'congrats').text)


