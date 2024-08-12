from selenium import webdriver
import os
import time
import math

from selenium.webdriver.common.by import By

try:
    browser = webdriver.Safari()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys('My name')
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys('My last name')
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys('My email')

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'lesson2_2_step8.txt')
    file_btn = browser.find_element(By.ID, "file")
    file_btn.send_keys(file_path)

    #browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    button2 = browser.find_element(By.TAG_NAME, "button")
    button2.click()
    assert True

finally:
    time.sleep(5)
    browser.quit()