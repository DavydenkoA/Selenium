'''
Модальные окна
Модальное окно — это окно, которое блокирует работу пользователя до тех пор, пока это окно не закроют. В этом степе
мы поговорим только про те окна, которые использует браузер. О тех, которые формируются при помощи JavaScript
создателями сайта, мы говорить не будем, но этими окнами можно управлять другими средствами Selenium, о которых
мы говорили в других уроках.

На сайте тренёжере можно посмотреть, как работают простые модальные окна, вшитые в браузер.

Основные функции применяемые к модальным окнам.

.switch_to - позволяет переключить фокус на модальное окно. Это необходимо, чтобы взаимодействовать с
содержимым этого окна.

# Переключение фокуса на модальное окно
driver.switch_to.alert
.accept() - имитирует нажатие на кнопку "ОК" в модальном окне. Обычно используется для подтверждения
какого-либо действия.

# Подтвердить содержимое модального окна
driver.switch_to.alert.accept()
.dismiss() - имитирует нажатие на кнопку "Отмена" в модальном окне. Позволяет отказаться от выполнения какого-либо
действия или закрыть окно без подтверждения.

# Или отклонить содержимое модального окна
driver.switch_to.alert.dismiss()
.send_keys() - позволяет отправить текст в текстовое поле внутри модального окна. Например, это может быть поле
для ввода пароля или комментария.

# Отправка текста в текстовое поле модального окна
driver.switch_to.alert.send_keys("Текст для отправки")
.text - возвращает заголовок (title) модального окна. Это может пригодиться для проверки того, что правильное
окно отображается на экране.

# Получение title модального окна
modal_title = driver.switch_to.alert.text

Переключение на все виды модальных окон выполняется командой browser.switch_to.alert

Виды модальных окон.
Alert - выводит пользователю сообщение, содержит кнопку "ОК";

Prompt - запрашивает у пользователя ввод каких-либо текстовых данных, содержит кнопки "ОК" и "Отмена";

Confirm - выводит окно с вопросом, содержит кнопки "ОК" и "Отмена".

Модальное окно Alert
Код, представленный ниже, выполняет клик на кнопку с id="alert", вызывая тем самым модальное окно alert.
Затем он переключается на это окно с помощью функции browser.switch_to.alert и выводит содержимое title этого окна.
'''
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/blank/modal/1/index.html')
#     browser.find_element(By.ID, 'alert').click()
#     time.sleep(1)
#     alert = browser.switch_to.alert # Если вы планируете что-то делать с этим событием, можно добавить его в переменную
#     print(alert.text)
#     time.sleep(1)
#     alert.accept()
#     time.sleep(1)
#
# >>> Это модальное окно alert
'''
Модальное окно Prompt
С помощью функции .send_keys("") можно отправлять текст в модальное окно prompt.
'''
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/blank/modal/1/index.html')
#     browser.find_element(By.ID, 'prompt').click()
#     time.sleep(2)
#     prompt = browser.switch_to.alert
#     prompt.send_keys('Введёный текст')
#     prompt.accept()
#     time.sleep(.5)
#     print(browser.find_element(By.ID, 'result').text)
#     time.sleep(1)
#
# >>> Введёный текст
'''
Приведённый выше код сначала нажимает на кнопку с id="prompt", вызывая модальное окно prompt. Затем он отправляет 
текст в текстовое поле этого окна и подтверждает ввод, нажимая кнопку "OK" с помощью функции .accept(). 
После того как кнопка "OK" была нажата, на странице в теге с id="result" отображается текст, введённый пользователем.

Столкнулись с проблемой при работе в Chrome: введённый текст в окне prompt не отображается, хотя вышеуказанный 
код возвращает нам введённое значение. Это подтверждает, что функция .send_keys() работает, но, возможно, 
не совсем корректно. Причиной может быть как Selenium, так и сам Chrome. Например, в браузерах Firefox или Opera 
такой проблемы не обнаружено.

Модальное окно Confirm
Модальное окно confirm имеет всего две кнопки: "Ok" и "Отмена". Взаимодействовать с ними можно с 
помощью функций .accept() и .dismiss().
'''
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/blank/modal/1/index.html')
#     browser.find_element(By.ID, 'confirm').click()
#     time.sleep(2)
#     prompt = browser.switch_to.alert
#     prompt.accept() #Замените на .dismiss() чтобы нажать на кнопку "Отмена"
#     time.sleep(.5)
'''
Код выше нажимает на кнопку Confirm и в появившемся окне — на кнопку Ok.
'''