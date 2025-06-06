'''
Размеры окна браузера
.set_window_size()
В различных ситуациях нам необходимо указывать собственный размер окна браузера. Например, когда вы запускаете скрипт
на компьютере с маленьким монитором или, наоборот, на огромном мониторе, или когда собираетесь открыть одновременно
большое количество окон браузера. Сценариев применения методов изменения размеров окна браузера множество.

Задать размер окна браузера можно методом driver.set_window_size(X, Y).

Где X – это ширина окна;

Где Y – это высота окна.

Важно знать, что минимальный размер окна браузера может быть следующим: ширина - 516px, высота - 134px, включая все
элементы управления браузера, а не только рабочую область сайта.
'''
# import time
# from selenium import webdriver
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/window_size/1/')
#     browser.set_window_size(1200, 720)
#     time.sleep(5)
'''
Код выше откроет окно браузера размером x:1200px,  y:720px.

Рабочая область сайта в данном случае будет равна x:1184px, y:587px. Не путайте с общим размером окна браузера. 
Данные получены с учетом 100% масштабирования экрана в Windows 10 при разрешении экрана Full HD (1920x1080). 
У вас эти числа могут отличаться.

16px занимают боковые границы браузера: левая и правая.
133px занимает верхняя панель управления браузера и нижняя граница.
Учитывайте эту особенность при написании кода для будущих парсеров и решения задач.

.get_window_size()
Для получения размеров окна браузера используется метод .get_window_size(). У него есть метод .get(), 
который принимает два параметра: 'height' и 'width' соответственно. Они возвращают высоту и ширину окна браузера.
Этот метод возвращает размер окна в виде словаря. {'width': 1202, 'height': 722}
'''
# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     # Открываем указанный URL в браузере.
#     browser.get('http://parsinger.ru/window_size/1/')

#     # Устанавливаем размер окна браузера на 1200 пикселей в ширину и 720 пикселей в высоту.
#     browser.set_window_size(1200, 720)
#
#     # Получаем текущий размер окна браузера в виде словаря, где 'height' - высота окна,
#     # 'width' - ширина окна. И затем печатаем значение высоты окна.
#     print(browser.get_window_size().get('height'))
#
#     # Аналогично печатаем значение ширины окна.
#     print(browser.get_window_size().get('width'))
#
# # После завершения выполнения кода в блоке 'with', браузер автоматически закрывается.

'''
.get_window_size().get('height'):

.get('height'): Метод get — это альтернативный способ извлечения значения из словаря. Он вернет значение, 
соответствующее ключу 'height', или None, если такого ключа нет в словаре. В данном контексте это выражение также 
вернет высоту окна браузера.
.get_window_size().get('width'):

.get('width'): Метод get извлекает значение из словаря по ключу 'width'. Таким образом, это выражение вернет ширину 
окна браузера. 

Как и при работе с любым словарем, мы можем получить доступ к ширине или высоте по ключу ["width"] и  ["height"].
'''
# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     # Загрузка указанного URL ('http://parsinger.ru/window_size/1/') в открытом окне браузера.
#     browser.get('http://parsinger.ru/window_size/1/')
#
#     # Установка размера окна браузера: ширина — 1200 пикселей и высота — 720 пикселей.
#     browser.set_window_size(1200, 720)
#
#     # Получение текущего размера окна браузера и вывод его ширины на экран.
#     # Обращаемся к ключу "width" в полученном словаре.
#     print(browser.get_window_size()["width"])
#
#     # Получение текущего размера окна браузера и вывод его высоты на экран.
#     # Обращаемся к ключу "height" в полученном словаре.
#     print(browser.get_window_size()["height"])
'''
get_window_size()["width"]:

["width"]: Это обращение к значению словаря по ключу "width". Это выражение вернет ширину окна браузера.
.get_window_size()["height"]:

["height"]: Это обращение к значению словаря по ключу "height". Это выражение вернет высоту окна браузера.
'''