from selenium.webdriver.common.by import By

# Кнопка Разместить объявление
CREATE_AD_BUTTON_WITH_AUTH = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
LOGIN_HEADER = (By.CSS_SELECTOR, ".h1")

# Инпуты
NAME_INPUT = (By.XPATH, ".//input[@placeholder = 'Название']")
DESCRIPTION_INPUT = (By.XPATH, ".//textarea[@placeholder = 'Описание товара']")
PRICE_INPUT = (By.NAME, "price")

# Dropdowns
CATEGORY_DROPDOWN = (By.XPATH, ".//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP'][1]")
CATEGORY_ITEM = (By.XPATH, ".//button[contains(., 'Книги')]")
CITY_DROPDOWN = (By.XPATH, ".//*[@id='root']/div/div[2]/div/form/div[3]/div[1]/button")
CITY_ITEM = (By.XPATH, ".//button[contains(., 'Нижний Новгород')]")

# Радиобаттон
CONDITION_RADIOBUTTON = (By.NAME, "condition")
BY_CHECKBOX = (By.XPATH, ".//label[text()='Б/У']/../div")
NEW_CHECKBOX = (By.XPATH, "label[text()='Новый']/../div")

# Кнопка Опубликовать
SUBMIT_BUTTON = (By.XPATH, ".//button[@type = 'submit']")

# Форма авторизации для создания объявления
FOR_CREATE_AD_AUTH_FORM = (By.XPATH, ".//form[@class='popUp_shell__LuyqR']/div/h1")
