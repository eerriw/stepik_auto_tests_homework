
    # https://stepik.org/lesson/181384/step/8?unit=156009

    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    # Нажать на кнопку "Book"
    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"


try: 
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()


    x_value = browser.find_element(By.ID, "input_value")
    x = x_value.text #Text from field
    answer = calc(x)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(answer) #Searching place where to send answer

    browser.find_element(By.ID, "solve").click()




finally:
    alert = WebDriverWait(browser, 15).until(EC.alert_is_present()) #wait until alert is present
    alert_text = alert.text #switch to alert tab and take text
    correct_answer = alert_text.split(": ")[-1]  #split the text with ': ' and choose last element
    alert.accept()
    print(correct_answer) #print answer in terminal
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()

