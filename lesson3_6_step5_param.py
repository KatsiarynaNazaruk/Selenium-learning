import time
import math
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_enter_correct_answer(browser, lesson):
	link = "https://stepik.org/lesson/{}/step/1".format(lesson)
	browser.get(link)

	# неявное ожидание появления элементов
	browser.implicitly_wait(5)

	# Подсчитать правильный ответ
	answer = math.log(int(time.time()))
	# Ввести ответ в текстовое поле
	text_area = browser.find_element_by_tag_name('textarea')
	text_area.send_keys(str(answer))

	# Нажать на кнопку Отправить
	button_send = browser.find_element_by_tag_name('button')
	button_send.click()

	# Найти появившееся поле с текстом и сравнить тест на значение
	correct_text_elt = browser.find_element_by_class_name('smart-hints__hint')
	# записываем в переменную welcome_text текст из элемента welcome_text_elt
	correct_text = correct_text_elt.text
	
	# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
	assert correct_text == "Correct!", "Текст:'{}' не совпадает у текстом успешного выполненного задания".format(correct_text)