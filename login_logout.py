from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
link = "https://magnusid-dev-services.mgns-tech.ru:8443/api/v1/login?service=https%3A%2F%2Fmagnusid-dev-services.mgns-tech.ru%3A8443%2Fapi%2Fv1%2Foauth2.0%2FcallbackAuthorize%3Fclient_id%3Dconsole-core-fron-dev%26scope%3Dopenid%26redirect_uri%3Dhttp%253A%252F%252Fmagnusid-dev-front.mgns-tech.ru%253A5173%26response_type%3Dcode%26client_name%3DCasOAuthClient"
browser.get(link)

button4 = browser.find_element(By.CSS_SELECTOR, "#details-button")
button4.click()

button5 = browser.find_element(By.CSS_SELECTOR, "#proceed-link")
button5.click()
i=1
for i in range(1,100):
    try:
        button1 = WebDriverWait(browser, timeout=30, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#login"))
        )
        button1.send_keys("d.chirkov")
        print("Элемент найден и кликнут!")
    except TimeoutException:
        print("Элемент не появился за 30 секунд")




    button2 = browser.find_element(By.CSS_SELECTOR, "#password")
    button2.send_keys("password1")
    button3 = browser.find_element(By.CSS_SELECTOR, "#login-button")
    button3.click()
    try:
        button6 = WebDriverWait(browser, timeout=30, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".v-avatar"))
        )
        button6.click()
        print("Элемент найден и кликнут!")
    except TimeoutException:
        print("Элемент не появился за 30 секунд")

    try:
        button7 = WebDriverWait(browser, timeout=30, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()=' Выйти ']"))
        )
        button7.click()
        print("Элемент найден и кликнут!")
    except TimeoutException:
        print("Элемент не появился за 30 секунд")

    i+=1



browser.quit()