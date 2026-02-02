import os
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

button_1=browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button_1.click()
confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
pole=browser.find_element(By.CSS_SELECTOR, "#answer")
pole.send_keys(y)
cx3=browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
cx3.click()


time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()
