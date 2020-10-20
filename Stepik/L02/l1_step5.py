import math

from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("//*[@id=\"input_value\"]")
    x = x_element.text
    y = calc(x)
    text = browser.find_element_by_css_selector("#answer.form-control")
    text.send_keys(y)
    checkbox = browser.find_element_by_css_selector("[for = 'robotCheckbox']")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("[for = 'robotsRule']")
    radiobutton.click()
    button = browser.find_element_by_xpath("//button[contains(text(),\"Submit\")]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
