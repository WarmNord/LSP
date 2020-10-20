import math

from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #Поиск картинки с необходимым атрибутом
    x_element = browser.find_element_by_id("treasure")
    #Получение значение атрибута
    x = x_element.get_attribute("valuex")
    y = calc(int(x))
    text = browser.find_element_by_id("answer")
    text.send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    button = browser.find_element_by_xpath("//button[contains(text(),\"Submit\")]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
