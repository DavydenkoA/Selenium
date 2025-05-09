import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Импортируем настройки Chrome
from tqdm import tqdm

chrome_options = Options()
chrome_options.add_argument("--headless")  # Включение Headless-режима
with webdriver.Chrome(options=chrome_options) as browser:
    browser.get('http://parsinger.ru/window_size/2/index.html')
    time.sleep(1)

    window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
    real_size_x = []
    real_size_y = []
    for x in tqdm(range(len(window_size_x))):
        x_real = browser.get_window_size().get('width')
        y_real = browser.get_window_size().get('height')
        x_in = browser.find_element(By.ID, 'width').text
        y_in = browser.find_element(By.ID, 'height').text
        delta_x = x_real - int(x_in[3:])
        delta_y = y_real - int(y_in[3:])

        # print(x_in[3:], y_in[3:], '  ', x_real, y_real, '  ', delta_x, delta_y)

        # browser.set_window_size(window_size_x[x], window_size_y[x])
        for r in tqdm(range(len(window_size_x))):
            browser.set_window_size(window_size_x[x] + delta_x, window_size_y[r] + delta_y)

            alrm = browser.find_element(By.ID, 'result').text
            # time.sleep(.1)
            if alrm:
                print(alrm)
                break

# решение проходит только если вытсавить масштабирование на ноутбуке 100%
# 9874163854135461654