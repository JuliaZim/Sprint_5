from selenium.webdriver.common.by import By

# Поля ввода
REGISTRATION_EMAIL_INPUT = (By.NAME, "email")
REGISTRATION_PASSWORD_INPUT = (By.NAME, "password")
SUBMIT_PASSWORD_INPUT = (By.NAME, "submitPassword")

# Кнопка Создать аккаунт
CREATE_ACCOUT_BUTTON = (By.XPATH, './/button[text()="Создать аккаунт"]')

# Ошибки
ERROR_EMAIL = (By.XPATH, ".//input[@placeholder='Введите Email']/parent::*")
ERROR_PASSWORD = (By.XPATH, ".//input[@name='password']/parent::*")
ERROR_SUBMIT_PASSWORD = (By.XPATH, ".//input[@name='submitPassword']/parent::*")
ERROR_TEXT_EMAIL = (By.XPATH, ".//div[@class='popUp_inputColumn__RgD8n']//div[1]//span")
