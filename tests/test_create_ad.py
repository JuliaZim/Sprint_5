from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators import main_page_locators
from ..locators import create_ad_locators
import random
from ..locators import profile_page_locators

class TestCreateAd:
    # Создание объявления неавторизованным пользователем
    def test_create_ad_noauth_client(self, browser):
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable(main_page_locators.CREATE_AD_BUTTON))

        # Кликаем на кнопку Разместить объявление
        browser.find_element(*main_page_locators.CREATE_AD_BUTTON).click()

        # Ожидаем форму авторизации
        wait.until(
            EC.visibility_of_element_located(create_ad_locators.FOR_CREATE_AD_AUTH_FORM)
        )
        create_ad_auth_form = browser.find_element(
            *create_ad_locators.FOR_CREATE_AD_AUTH_FORM
        )

        # Проверяем, что форма регистрации отображается
        assert (
            create_ad_auth_form.is_displayed
            and create_ad_auth_form.text == "Чтобы разместить объявление, авторизуйтесь"
        )

    # Создание объявления авторизованным пользователем
    def test_create_ad_auth_client(self, browser, registration_new_user):
        email, password = registration_new_user
        wait = WebDriverWait(browser, 20)
        element = browser.find_element(*create_ad_locators.CREATE_AD_BUTTON_WITH_AUTH)
        wait.until(EC.staleness_of(element))
        # Кликаем на кнопку Разместить объявление
        wait.until(EC.element_to_be_clickable(create_ad_locators.CREATE_AD_BUTTON_WITH_AUTH))
        browser.find_element(*create_ad_locators.CREATE_AD_BUTTON_WITH_AUTH).click()
       
        wait.until(EC.element_to_be_clickable(create_ad_locators.SUBMIT_BUTTON))

        # Присваиваем значения для полей ввода
        name_product = f"Товар {random.randint(100, 1000)}"
        description_product = f"Описание товара {random.randint(100, 1000)}"
        price_product = random.randint(100, 10000)

        # заполняем поля ввода
        browser.find_element(*create_ad_locators.NAME_INPUT).send_keys(name_product)
        browser.find_element(*create_ad_locators.DESCRIPTION_INPUT).send_keys(
            description_product
        )
        browser.find_element(*create_ad_locators.PRICE_INPUT).send_keys(price_product)

        # Заполняем DropDownы
        # заполняем dropdown Категория
        browser.find_element(*create_ad_locators.CATEGORY_DROPDOWN).click()
        wait.until(EC.element_to_be_clickable(create_ad_locators.CATEGORY_ITEM))
        browser.find_element(*create_ad_locators.CATEGORY_ITEM).click()

        # Заполняем dropdown город
        wait.until(EC.element_to_be_clickable(create_ad_locators.CITY_DROPDOWN))
        browser.find_element(*create_ad_locators.CITY_DROPDOWN).click()
        wait.until(EC.element_to_be_clickable(create_ad_locators.CITY_ITEM))
        browser.find_element(*create_ad_locators.CITY_ITEM).click()
     
        # Кликаем в чекбокс Б/У
        browser.find_element(*create_ad_locators.BY_CHECKBOX).click()

        # Кликаем Опубликовать
        wait.until(EC.element_to_be_clickable(create_ad_locators.SUBMIT_BUTTON))
        browser.find_element(*create_ad_locators.SUBMIT_BUTTON).click()
        
        # Заходим в свой профиль
        element1 = browser.find_element(*main_page_locators.AVATAR)
        wait.until(EC.staleness_of(element1))
        browser.find_element(*main_page_locators.AVATAR).click()
        wait.until(EC.visibility_of_element_located(profile_page_locators.NAME_AD))

        #Вытскиваем значения имени товара и цены
        ad_name = browser.find_element(*profile_page_locators.NAME_AD).text
        ad_price = browser.find_element(*profile_page_locators.PRICE_AD).text
        #Для успешной проверки удаляем все пробелы из цены
        ad_price = ad_price.replace(" ", '')
        
        #Выполняем проверку имени товара и цены
        assert ad_name == name_product
        assert str(price_product) in ad_price
