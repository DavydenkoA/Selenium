from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://ya.ru/')
    cookies = webdriver.get_cookies()
    for cookie in cookies:
        print(cookie['name']) # или cookie['value'] чтобы получить их значение
# >>>
# _ym_d, _ym_isad, _ym_uid, my, gdpr, _yasc, i, is_gdpr, yuidss
# yabs-frequency, is_gdpr_b, yandexuid, yp, mda, ymex, yandex_gid