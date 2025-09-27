from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators import login_page_locators
from ..locators import main_page_locators
from selenium.common.exceptions import NoSuchElementException


class TestLoginPage:
    # Логин
    def test_login_success(self, browser, registration_new_user):
        email, password = registration_new_user
        wait = WebDriverWait(browser, 10)

        #Выходим из аккаунта
        wait.until(EC.element_to_be_clickable(main_page_locators.EXIT_BUTTON))
        browser.find_element(*main_page_locators.EXIT_BUTTON).click()
        wait.until(EC.element_to_be_clickable(login_page_locators.LOGIN_AND_REGISTRATION_BUTTON))
        # Кликаем на кнопку Вход и регистрация
        browser.find_element(*login_page_locators.LOGIN_AND_REGISTRATION_BUTTON).click()

        # Заполняем поля
        browser.find_element(
            *login_page_locators.LOGIN_EMAIL_INPUT
        ).send_keys(email)
        browser.find_element(
            *login_page_locators.LOGIN_PASSWORD_INPUT
        ).send_keys(password)

        # Кликаем кнопку Войти
        browser.find_element(*login_page_locators.LOGIN_BUTTON).click()

        # Проверка, что произошел вход, есть фото профиля и имя USER
        wait.until(EC.presence_of_element_located(main_page_locators.USER))

        assert (
            browser.find_element(*main_page_locators.CREATE_AD_BUTTON).is_displayed()
            and browser.find_element(*main_page_locators.USER).text == "User."
            and browser.find_element(*main_page_locators.AVATAR).is_displayed()
        )

    # Logout
    def test_logout_success(self, browser, registration_new_user):
        email, password = registration_new_user
        wait = WebDriverWait(browser, 10)

        #Выходим из аккаунта
        wait.until(EC.element_to_be_clickable(main_page_locators.EXIT_BUTTON))
        browser.find_element(*main_page_locators.EXIT_BUTTON).click()
        
        # Проверка, что произошел вход, есть фото профиля и имя USER
        wait.until(EC.presence_of_element_located(main_page_locators.USER))
        
        try:
            user_text = browser.find_element(*main_page_locators.USER).text
            avatar_displayed = browser.find_element(*main_page_locators.AVATAR).is_displayed()
            login_button_displayed = browser.find_element(*login_page_locators.LOGIN_AND_REGISTRATION_BUTTON).is_displayed()
            create_ad_button_displayed = browser.find_element(*main_page_locators.CREATE_AD_BUTTON).is_displayed()
        except NoSuchElementException:
            user_text = False
            avatar_displayed = False
            login_button_displayed = True
            create_ad_button_displayed = False

        assert not create_ad_button_displayed, "Кнопка 'Создать объявление' отображается, хотя не должна."
        assert not user_text, "Текст пользователя 'User.' отображается, хотя не должен."
        assert not avatar_displayed, "Аватар отображается, хотя не должен."
        assert login_button_displayed, "Кнопка 'Войти и зарегистрироваться' не отображается, хотя должна."
            