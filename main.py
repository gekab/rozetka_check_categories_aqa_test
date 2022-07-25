import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def proverka(ex_res, act_res):
    return f"Тест пройден успешно, {ex_res} = {act_res}" if ex_res == act_res else f"Тест провален, {ex_res} <> {act_res}"

link = "https://rozetka.com.ua/"
browser = webdriver.Chrome()
browser.maximize_window()

browser.get(link)
category_menu = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'ul[class*=menu-categories_type_main]>li')))
call_elem_menu = len(category_menu)
for elem in range(call_elem_menu):
    category_menu = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'ul[class*=menu-categories_type_main]>li')))
    expected_result = category_menu[elem].text
    print(f'-----Тест №{elem}')
    print('Ожидаемый результат: ', expected_result)
    category_menu[elem].click()
    time.sleep(2)
    try:
        actual_result = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1[class*=ng-star-inserted]')))
        actual_result = actual_result.text
        print('Фактический результат: ', actual_result, '\n')
        print(proverka(expected_result, actual_result))
    except Exception as _ex:
        print(f'Нет Заголовка H1 с текстом \'{expected_result}\' на странице \'{browser.title}\', ошибка: ', _ex)
    finally:
        actual_result = f'Нет заголовка на странице \'{browser.title}\''

    browser.back()
