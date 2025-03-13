from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_element = browser.find_element(By.ID, "num1")
    x1 = first_element.text
    second_element = browser.find_element(By.ID, "num2")
    x2 = second_element.text
    y = int(x1) + int(x2)

    # Ваш код, который заполняет обязательные поля
    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(y))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
