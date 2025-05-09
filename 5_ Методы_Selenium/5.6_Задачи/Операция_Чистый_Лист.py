'''
Приветствую, кодовые ниндзя! Сегодня перед вами стоит задача, которую можно сравнить с миссией по деминированию — 
только вместо бомб у нас текстовые поля, и взрывать ничего не будем. Но задача не менее интригующая! Суть в том, 
чтобы научиться быстро и эффективно взаимодействовать с элементами на веб-странице. Ведь в реальных проектах 
скорость часто имеет решающее значение.
Задачи
На старт, внимание, марш!: Откройте указанную веб-страницу с помощью Selenium
https://parsinger.ru/selenium/5.5/1/1.html
 
Операция 'Чистый Лист': На странице расположены 100 текстовых полей с текстом. Ваша задача — пройтись по каждому 
и удалить его содержимое. Причём быстро, у вас всего 5 секунд!
Завершающий этап: После того как все поля будут очищены, нажмите на кнопку на странице.
Секретный Код: Скопируйте число, которое появится во всплывающем alert-окне, с помощью Selenium.
Результат: Вставьте полученное число в поле ответа степик.
Для очистки текстового поля используйте: 
field.clear()
Для переключения на alert-окно и получения текста из него, используйте:
# Переключаемся на алерт и получаем его текст
alert = driver.switch_to.alert.text
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

# скрытый режим
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--headless=new')
#with webdriver.Chrome(options=options_chrome) as browser:
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/1/1.html')
    elements = browser.find_elements(By.CLASS_NAME, 'text-field')
    for x in elements:
        x.clear()
    browser.find_element(By.ID, 'checkButton').click()
    print(browser.switch_to.alert.text)

