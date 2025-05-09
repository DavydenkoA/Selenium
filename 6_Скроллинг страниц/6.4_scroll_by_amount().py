'''
В версии Selenium 4.2 появился замечательный метод .scroll_by_amount(), который позволяет скролить любое окно на
заданное количество пикселей. Этот метод намного упрощает взаимодействие с окнами, в которых присутствует элемент
скроллинга. Чтобы этот метод заработал, обновите ваш selenium до последней версии.
scroll_by_amount(delta_x, delta_y) -
- delta_x: расстояние по оси X для прокрутки с помощью колеса. Отрицательное значение прокручивается влево.
- delta_y: расстояние по оси Y для прокрутки с помощью колеса. Отрицательное значение прокручивается вверх.
Этот метод работает в цепочке событий ActionChains.
'''

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
#
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_2/')
#     div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
#     while True:
#         ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()

'''
Как это работает: 
В переменной div мы определяем окно, которое мы собираемся прокручивать, оно должно иметь полосу прокрутки, иначе 
ничего не произойдет.
Цикл while для постоянной прокрутки, без цикла скроллинг происходит один раз, что не подойдет для бесконечно 
подгружаемых элементов.
ActionChains(browser) - создаем цепочку событий.
.move_to_element(div) - перемещаемся к элементу веб драйвера, который мы записали в переменную div.
.scroll_by_amount(1, 500)  - скроллинг применяется к элементу в методе  .move_to_element(div).
Как итог, мы получаем код, который бесконечно скролит элемент, и нужно думать над его прерыванием. Если мы знаем, 
какой длины список, мы можем использовать цикл for. Если вы уверены, что вам хватит прокрутить элемент 10 раз по 500px, 
то можно использовать такой подход.
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_2/')
    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
    for x in range(10):
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()