# Решение финального проекта 5 спринта

Необходимо реализовать 7 тестов для сайта https://qa-desk.stand.praktikum-services.ru/

## Описание файлов
test - общая директория с тестами  
* locators - папка с локаторами  
* conftest.py - файл с фикстурами  
* test_create_ad.py - тесты для функционала размещения объявлений
* test_login_page.py - Тесты для функционала логина\логаута
* test_registration.py - тесты для функционала регистрации пользователя

Папка locators содержит несколько файлов для разных страниц:
* CreateAdLocators.py - локаторы для создания объявления
* LoginPageLocators.py - локаторы login
* MainPageLocators - локаторы главной страницы
* ProfilePageLocators.py - локаторы профиля
R* egistrationPageLocators.py - локаторы регистрации

### Тесты

test_registration.py  
* test_registration_succes - регистрация нового пользователя  
* test_registration_with_incorrect_email - Регистрация пользователя с email не по маске  
* test_registration_exist_user - Регистрация уже существующего пользователя

test_login_page.py  
* test_login_success - Проверка успешного логина
* test_logout_success - Проверка логаута

test_create_ad.py  
* test_create_ad_noauth_client - Создание объявления неавторизованным пользователем
* test_create_ad_auth_client - Создание объявления авторизованным пользователем
