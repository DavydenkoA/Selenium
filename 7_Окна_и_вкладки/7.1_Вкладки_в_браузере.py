'''
Вкладки в браузере
При работе в браузере мы можем открывать новые вкладки и работать в них. Можем открыть любое количество вкладок
одновременно, но работать можем только в активной. Мы можем переключаться между вкладками, получать их title,
проходить по вкладкам в цикле, получать их дескрипторы — практически все то, что вы делаете вручную.

Вам может понадобиться собрать данные со второй вкладки, не отвлекаясь на первую. Или сайт, который вы парсите,
открывает ссылки в новой вкладке. Такое происходит, если у ссылок есть атрибут target="_blank".

Дескриптор — это идентификатор вкладки браузера. В Opera и Chrome дескрипторы выглядят одинаково, например,
CDwindow-8696D8A3F222B281BB03FC1EC259B251, а в Firefox они имеют иной вид, например,
d8e0e954-bf72-4eae-a63e-5ea404c3b0eb. Дескрипторы — это те сущности, которые помогают нам манипулировать вкладками.

.current_window_handle — возвращает дескриптор текущей вкладки;
.window_handles — возвращает список всех дескрипторов открытых вкладок;
.switch_to.window(window_handles[0]) — переключает фокус между вкладками.
Исправленный вариант:

Запустите код ниже, чтобы посмотреть, как он работает. Этот код открывает первую вкладку методом .get("URL"),
затем открывает ещё три вкладки методом .execute_script() и после этого печатает все дескрипторы открытых вкладок.
'''
# import time
# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     result = []
#     browser.get('http://parsinger.ru/blank/2/1.html')
#     time.sleep(1)
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank1");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank2");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank3");')
#     time.sleep(2)
#     print(browser.window_handles)

#c>>> ['CDwindow-FB580151A416179D7204A36722F50B18', 'CDwindow-12E90DEA6DFEE366B620282C8A228131',
# 'CDwindow-92FEA4784AB5E877CE8ADCF42D1FB1DE', 'CDwindow-75AB8AC2EFB6B091AC149C007E9B787B',
# 'CDwindow-F69371F46370168A1F355842C8F4A4AD']

'''
В некоторых гайдах в интернете вы будете встречать информацию о том, что работать можно только в первой открытой 
вкладке, а остальные открываются лишь для красоты. Но хочу вас обрадовать: это совсем не так. Работать мы можем 
со всеми вкладками, но только по очереди и только в активной.

Запустите у себя в терминале код ниже, чтобы наблюдать за работой Selenium во всех вкладках по очереди. Обратите 
внимание на то, что мы получаем длину списка. Также заметьте, что итерация по вкладкам происходит в обратном порядке — 
от последней к первой. Чтобы этого избежать, просто добавьте к циклу функцию reversed(). Следует также учесть, что 
самая первая вкладка имеет имя "data"; в этой вкладке открывается страница, переданная в метод .get("URL").
'''
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as browser:
    #browser.get("https://stepik.org/course/104774/promo") # Вместо вкладки data; будет вкладка
    # в которой будет загружен степик
    # browser.execute_script('window.open("http://parsinger.ru/blank/2/1.html", "_blank1");')
    # browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank2");')
    # browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank3");')
    # browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank4");')

    # for x in range(len(browser.window_handles)):  #reversed(range(len(browser.window_handles)))
        # Для итерирования по порядку
        # browser.switch_to.window(browser.window_handles[x])
        # for y in browser.find_elements(By.CLASS_NAME, 'check'):
        #     y.click()

'''
Чтобы лучше понять, как происходит итерирование по вкладкам, я создал следующий пример. Запустите код ниже у себя в 
терминале и посмотрите на процесс итерирования. Также обратите внимание на то, что вкладка с именем "data" не 
возвращает своего имени, так как не содержит тега <title>.
'''
# import time
# from selenium import webdriver
# with webdriver.Chrome() as browser:
#     time.sleep(1)
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/1.html", "_blank1");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/2.html", "_blank2");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/3.html", "_blank3");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/4.html", "_blank4");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/5.html", "_blank5");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/0/6.html", "_blank6");')
#
#     for x in range(len(browser.window_handles)):
#         browser.switch_to.window(browser.window_handles[x])
#         time.sleep(1)
#         print(browser.execute_script("return document.title;"), browser.window_handles[x])

'''
Получаем title вкладки
Title — это то, что содержится в HTML-тегах <title>Текст на вкладке</title> и отображается на вкладке браузера.

Чтобы получить имя вкладки, т.е. её title, используется метод .execute_script("return document.title;"), в 
который мы передали код JavaScript, возвращающий имя вкладки.

Запустите код ниже у себя в терминале. Этот код откроет "степик" и напечатает вам в консоли title вкладки.
'''

# from selenium import webdriver
# with webdriver.Chrome() as browser:
#     browser.get("https://stepik.org/course/104774/promo")
#     print(browser.execute_script("return document.title;"))

#>>> WEB Парсинг на Python — Stepik