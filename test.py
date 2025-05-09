from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/5/index.html')
    frame = browser.find_elements(By.TAG_NAME, 'iframe')

    for x in frame:
        browser.switch_to.frame(x.get_attribute('id'))
        browser.find_element(By.TAG_NAME, 'button').click()
        dig = browser.find_element(By.ID, 'numberDisplay').text
        browser.switch_to.default_content()
        browser.find_element(By.ID, 'guessInput').clear()
        browser.find_element(By.ID, 'guessInput').send_keys(dig)
        browser.find_element(By.ID, 'checkBtn').click()
        try:
            print(browser.switch_to.alert.text)
        except:
            pass