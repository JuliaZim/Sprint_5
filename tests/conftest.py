from selenium import webdriver
import pytest
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import login_page_locators
from locators import registration_page_locators


# Фикстура для запуска и закрытия браузера
@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    yield driver
    driver.quit()

# Фикстура для появления окна с регистрацией
@pytest.fixture(scope='function')
def registration_popup(browser):
    wait = WebDriverWait(browser, 10)
    # Ждем пока кнопка Вход и регистрация будет кликабельна
    wait.until(EC.element_to_be_clickable(login_page_locators.LOGIN_AND_REGISTRATION_BUTTON))
    # Кликаем на кнопку Вход и регистрация
    browser.find_element(*login_page_locators.LOGIN_AND_REGISTRATION_BUTTON).click()
    #Ждем пока кнопка "Нет аккаунта" будет кликабельна
    wait.until(EC.element_to_be_clickable(login_page_locators.NOT_EXIST_ACOUNT_BUTTON))
    # Кликаем на кнопку Нет аккаунта
    browser.find_element(*login_page_locators.NOT_EXIST_ACOUNT_BUTTON).click()
    return browser

# Фикстура регистрации нового пользователя
@pytest.fixture(scope='function')
def registration_new_user(browser):
    wait = WebDriverWait(browser, 10)
    # Ждем пока кнопка Вход и регистрация будет кликабельна
    wait.until(EC.element_to_be_clickable(login_page_locators.LOGIN_AND_REGISTRATION_BUTTON))
    # Кликаем на кнопку Вход и регистрация
    browser.find_element(*login_page_locators.LOGIN_AND_REGISTRATION_BUTTON).click()
    #Ждем пока кнопка "Нет аккаунта" будет кликабельна
    wait.until(EC.element_to_be_clickable(login_page_locators.NOT_EXIST_ACOUNT_BUTTON))
    # Кликаем на кнопку Нет аккаунта
    browser.find_element(*login_page_locators.NOT_EXIST_ACOUNT_BUTTON).click()
    email = f"test{random.randint(100, 1000)}@test.ru"
    password = str(random.randint(100000, 1000000))
    # Заполняем поля
    browser.find_element(
        *registration_page_locators.REGISTRATION_EMAIL_INPUT
    ).send_keys(email)
    browser.find_element(
        *registration_page_locators.REGISTRATION_PASSWORD_INPUT
    ).send_keys(password)

    browser.find_element(*registration_page_locators.SUBMIT_PASSWORD_INPUT).send_keys(
        password
    )
    # Кликаем кнопку Создать аккаунт
    browser.find_element(*registration_page_locators.CREATE_ACCOUT_BUTTON).click()
    return email, password 
    