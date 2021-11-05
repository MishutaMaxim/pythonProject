from selenium import webdriver
import time

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys('Vladimir')
    browser.find_element(By.CSS_SELECTOR, '.first_block > .second_class > input').send_keys('Putin')
    browser.find_element(By.CSS_SELECTOR, '.first_block > .third_class > input').send_keys('vova@molodec.ru')
    browser.find_element(By.CSS_SELECTOR, '.first_block > .third_class > input').send_keys('111')
    browser.find_element(By.CSS_SELECTOR, '.second_block > .second_class > input').send_keys('Kremlin')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
