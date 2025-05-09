import time
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('coordinates.crx')

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/course/104774'
    browser.get(url)
    time.sleep(15)

# в нашем случае расширение для Google Chrome Mouse Coordinates
# 0.2_0.crx  - упакованное расширение которое я переименовал в
# coordinates.crx, т.к. этот файл лежит в папке с проектом
# или указываем полный путь до файла
# C:\Users\[имя вашего пользователя]\AppData\Local\
# Google\Chrome\User Data\Default\Extensions\ghbmnnjooekpmoecnnnilnnbdlolhkhi\