from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators import login_page_locators
from ..locators import registration_page_locators
from ..locators import main_page_locators
import pytest
import random


class TestRegistration:
    
    # Регистрация нового пользователя
    def test_registration_success(self, browser, registration_popup):
        driver = browser
        wait = WebDriverWait(driver, 10)
        # Задаем логин и пароль
        email = f"test{random.randint(1000, 10000)}@test.ru"
        password = str(random.randint(100000, 1000000))

        # Заполняем поля
        driver.find_element(*registration_page_locators.REGISTRATION_EMAIL_INPUT).send_keys(email)
        driver.find_element(
            *registration_page_locators.REGISTRATION_PASSWORD_INPUT
        ).send_keys(password)
        driver.find_element(*registration_page_locators.SUBMIT_PASSWORD_INPUT).send_keys(
            password
        )

        # Кликаем кнопку Создать аккаунт
        driver.find_element(*registration_page_locators.CREATE_ACCOUT_BUTTON).click()

        # Проверка, что произошел вход, есть фото профиля и имя USER
        wait.until(EC.presence_of_element_located(main_page_locators.USER))
        assert (
            driver.find_element(*main_page_locators.CREATE_AD_BUTTON).is_displayed()
            and driver.find_element(*main_page_locators.USER).text == "User."
            and driver.find_element(*main_page_locators.AVATAR).is_displayed()
        )
        
    # Регистрация пользователя с email не по маске
    def test_registration_with_incorrect_email(self, registration_popup):
        
        driver = registration_popup
        wait = WebDriverWait(driver, 10)
        email = f"test{random.randint(100, 1000)}"
        password = str(random.randint(100000, 1000000))
        
        # Заполняем поля
        driver.find_element(
            *registration_page_locators.REGISTRATION_EMAIL_INPUT
        ).send_keys(email)
        driver.find_element(
            *registration_page_locators.REGISTRATION_PASSWORD_INPUT
        ).send_keys(password)

        driver.find_element(*registration_page_locators.SUBMIT_PASSWORD_INPUT).send_keys(
            password
        )

        # Кликаем кнопку Создать аккаунт
        driver.find_element(*registration_page_locators.CREATE_ACCOUT_BUTTON).click()

        # Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка».
        #  error_text = driver.find_element(*RegistrationPageLocators.ERROR_TEXT_EMAIL)

        error_email = wait.until(EC.visibility_of_element_located(registration_page_locators.ERROR_EMAIL))
        error_password_parent = wait.until(EC.visibility_of_element_located(registration_page_locators.ERROR_PASSWORD))
        error_submit_password_parent = wait.until(EC.visibility_of_element_located(registration_page_locators.ERROR_SUBMIT_PASSWORD))
        error_email_text = wait.until(EC.visibility_of_element_located(registration_page_locators.ERROR_TEXT_EMAIL))

            # Проверяем, что элемент с ошибкой отображается
        assert error_email.get_attribute("class") == 'input_inputError__fLUP9', "Текст ошибки email не отображается"
        assert error_password_parent.get_attribute('class') == 'input_inputError__fLUP9', "Поле password не подсвечено красным"
        assert error_submit_password_parent.get_attribute('class') == 'input_inputError__fLUP9', "Поле submit_password не подсвечено красным"
        assert error_email_text.is_displayed() and error_email_text.text == 'Ошибка'

    # Регистрация уже существующего пользователя
    def test_registration_exist_user(self, browser, registration_new_user):
        # Получаем email и password из фикстуры
        email, password = registration_new_user 
        wait = WebDriverWait(browser, 10)

        #Выходим из аккаунта
        wait.until(EC.element_to_be_clickable(main_page_locators.EXIT_BUTTON))
        browser.find_element(*main_page_locators.EXIT_BUTTON).click()
        wait.until(EC.element_to_be_clickable(login_page_locators.LOGIN_AND_REGISTRATION_BUTTON))
        # Кликаем на кнопку Вход и регистрация
        browser.find_element(*login_page_locators.LOGIN_AND_REGISTRATION_BUTTON).click()
        #Ждем пока кнопка "Нет аккаунта" будет кликабельна
        wait.until(EC.element_to_be_clickable(login_page_locators.NOT_EXIST_ACOUNT_BUTTON))
        # Кликаем на кнопку Нет аккаунта
        browser.find_element(*login_page_locators.NOT_EXIST_ACOUNT_BUTTON).click()

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
        
        error_email = wait.until(EC.visibility_of_element_located(registration_page_locators.ERROR_EMAIL))
        error_password_parent = wait.until(EC.visibility_of_element_located(registration_page_locators.ERROR_PASSWORD))
        error_submit_password_parent = wait.until(EC.visibility_of_element_located(registration_page_locators.ERROR_SUBMIT_PASSWORD))
        error_email_text = wait.until(EC.visibility_of_element_located(registration_page_locators.ERROR_TEXT_EMAIL))

            # Проверяем, что элемент с ошибкой отображается
        assert error_email.get_attribute("class") == 'input_inputError__fLUP9', "Текст ошибки email не отображается"
        assert error_password_parent.get_attribute('class') == 'input_inputError__fLUP9', "Поле password не подсвечено красным"
        assert error_submit_password_parent.get_attribute('class') == 'input_inputError__fLUP9', "Поле submit_password не подсвечено красным"
        assert error_email_text.is_displayed() and error_email_text.text == 'Ошибка'

