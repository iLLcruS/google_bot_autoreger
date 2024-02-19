import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
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
                f"\nPassword: {self.password}")


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
        # Ждем, пока кнопка "Далее" станет кликабельной
        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Далее')]/ancestor::button"))
        )
        # Нажимаем на кнопку
        next_button.click()
        time.sleep(50)

        # Здесь можете добавить дальнейшие действия, например, ввод даты рождения
    except Exception as e:
        print(f"Ошибка при попытке нажать на кнопку 'Далее': {e}")
