from selenium.webdriver.common.by import By

# кнопка Войти или зарегистрироваться
LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, './/button[text()="Вход и регистрация"]')
# Кнопка Нет аккаунта
NOT_EXIST_ACOUNT_BUTTON = (By.XPATH, './/button[text()="Нет аккаунта"]')
# Поля для заполнения
LOGIN_EMAIL_INPUT = (By.NAME, "email")
LOGIN_PASSWORD_INPUT = (By.NAME, "password")
# Кнопка Войти
LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')
