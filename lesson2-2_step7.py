
    # Открыть страницу http://suninjuly.github.io/file_input.html
    # Заполнить текстовые поля: имя, фамилия, email
    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    # Нажать кнопку "Submit"


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender


link = "http://suninjuly.github.io/file_input.html"


try: 
    browser = webdriver.Chrome()
    browser.get(link)

    person = Person(Locale.RU)
    first_name = person.first_name(gender = Gender.MALE)
    last_name = person.last_name(gender = Gender.MALE)
    email = person.email()
    
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys(first_name) #Searching place where to send first_name
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys(last_name) #Searching place where to send last_name
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys(email) #Searching place where to send email

    upload_file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    upload_file.send_keys(file_path)

    button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()

    time.sleep(3)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()

