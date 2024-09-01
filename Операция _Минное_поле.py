'''
Привет, будущие автоматизаторы! Сегодня у нас не просто задача, а настоящий тайм-триал, испытание на скорость и
точность! Мы переносимся в мир, где каждое неверное движение может стать последним... ну, или по крайней мере,
приведёт к неудачному выполнению задания. Задача симулирует реальную рабочую ситуацию, в которой на скорость
выполнения операций поставлен жесткий лимит.
Задачи
Стартовая Позиция: Используя Selenium, откройте заданный веб-сайт:
https://parsinger.ru/selenium/5.5/2/1.html
Убедитесь, что ваша машина готова к операции.

Секунды на Счетчике: У вас есть ровно 5 секунд, чтобы пройтись по ячейкам на странице и очистить только те,
которые доступны для редактирования.
Проверка: Нажмите на кнопку "Проверить" на странице.
Секретный код: Из всплывающего алерт-окна скопируйте код и вставьте его в поле для ответа.
Для проверки доступности текстового поля, используйте проверку атрибута disabled у соответствующих текстовых полей:

.get_attribute('disabled')
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

# скрытый режим
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--headless=new')
#with webdriver.Chrome(options=options_chrome) as browser:
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/2/1.html')
    elements = browser.find_elements(By.XPATH, '//*[@data-enabled="true"]')
    for x in elements:
        x.clear()

    browser.find_element(By.ID, 'checkButton').click()
    print(browser.switch_to.alert.text)
