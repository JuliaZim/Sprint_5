from selenium.webdriver.common.by import By

# Имя товара
NAME_AD = (By.XPATH, ".//div[@class='card'][last()]/div[@class='description']/div[@class='about']/h2")
# Цена товара
PRICE_AD = (By.XPATH, ".//div[@class='card'][last()]/div[@class='description']/div[@class='price']/h2")
