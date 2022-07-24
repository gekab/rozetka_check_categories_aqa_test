from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

link = "https://rozetka.com.ua/"
browser = webdriver.Chrome()
browser.maximize_window()
try:
    browser.get(link)
except Exception as _ex:
    print("Не удалось открыть сайт, ошибка: ", _ex)
finally:
    browser.close()
