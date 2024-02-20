import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from utils.utils import *


class RegistrationData:
    def __init__(self):
        self.first_name = generate_random_first_name()
        self.last_name = generate_random_last_name()
        self.email = generate_random_email()
        self.password = generate_random_password(12)
        self.day = generate_random_day()
        self.month = generate_random_month()
        self.year = generate_random_year()

    def input_first_and_last_name(self, driver):
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='firstName']"))
        ).clear()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='firstName']"))
        ).send_keys(self.first_name)

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='lastName']"))
        ).clear()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='lastName']"))
        ).send_keys(self.last_name)
        navigate_to_input_birth_date(driver)


    def output_data(self):
        return (f"First Name: {self.first_name}"
                f"\nLast Name: {self.last_name}"
                f"\nEmail: {self.email}"
                f"\nPassword: {self.password}"
                f"f\nDate: {self.day} / {self.month} / {self.year}")


def start_registration_engine_sync():
    registration_data = RegistrationData()
    driver = webdriver.Chrome()
    driver.get('https://google.com')
    login_button = driver.find_element(By.XPATH, "//a[contains(@href, 'ServiceLogin')]")
    login_button.click()

    navigate_to_create_link(driver, registration_data)


def navigate_to_create_link(driver, registration_data):
    try:
        create_account_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Создать аккаунт')]"))
        )
        create_account_button.click()

        for_personal_use_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Для личного использования')]"))
        )
        for_personal_use_option.click()
        registration_data.input_first_and_last_name(driver)

    except Exception as e:
        print(f"Ошибка при попытке нажать на кнопку 'Создать аккаунт': {e}")


def navigate_to_input_birth_date(driver):
    try:
        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Далее')]/ancestor::button"))
        )
        next_button.click()
        registration_data = RegistrationData()

        input_birth_date_and_gender(driver, registration_data=registration_data)

    except Exception as e:
        print(f"Ошибка при попытке нажать на кнопку 'Далее': {e}")

def input_birth_date_and_gender(driver, registration_data):
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "day"))
    ).send_keys(registration_data.day)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "month"))
    )
    Select(driver.find_element(By.ID, "month")).select_by_value(registration_data.month)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "year"))
    ).send_keys(registration_data.year)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "gender"))
    )
    Select(driver.find_element(By.ID, "gender")).select_by_index(random.randint(1, 3))  # Предполагая, что есть 3 опции
    navigate_to_next_page(driver)

    input_random_email(driver, registration_data)


def navigate_to_next_page(driver):
    try:
        next_button = WebDriverWait(driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Далее')]"))
        )
        next_button.click()

    except Exception as e:
        print(f"Ошибка при попытке нажать на кнопку 'Далее': {e}")


def input_random_email(driver, registration_data):
    email_input_xpath = "//input[@name='Username']"

    try:
        email_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, email_input_xpath))
        )
        email_input.clear()

        email_input.send_keys(registration_data.email.split('@')[0])

        navigate_to_next_page(driver)
        input_password_and_confirm(driver, registration_data)
    except Exception as e:
        print(f"Ошибка при попытке ввода электронной почты: {e}")


def input_password_and_confirm(driver, registration_data):
    password_input_xpath = "//input[@name='Passwd']"
    confirm_password_input_xpath = "//input[@name='PasswdAgain']"

    try:
        password_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, password_input_xpath))
        )
        password_input.clear()
        password_input.send_keys(registration_data.password)

        confirm_password_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, confirm_password_input_xpath))
        )
        confirm_password_input.clear()
        confirm_password_input.send_keys(registration_data.password)
        data = registration_data.output_data()
        print(data)
        time.sleep(5)
        navigate_to_next_page(driver)

        time.sleep(900)

    except Exception as e:
        print(f"Ошибка при попытке ввода пароля: {e}")
