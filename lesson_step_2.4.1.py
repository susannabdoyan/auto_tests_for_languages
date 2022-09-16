from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/cats.html")


    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

    text = browser.switch_to.alert.text
    code = text.split(" ")[-1]
    print(code)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


