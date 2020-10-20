from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #Поиск num1
    num1 = int(browser.find_element_by_id("num1").text)
    #Поиск num2
    num2 = int(browser.find_element_by_id("num2").text)

    y = num1 + num2

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(y))

    button = browser.find_element_by_xpath("//button[contains(text(),\"Submit\")]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
