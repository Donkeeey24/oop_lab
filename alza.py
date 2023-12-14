from selenium import webdriver
from selenium.webdriver.common.by import By
url = "https://www.alza.cz/samsung-galaxy-tab-s9-ultra-wifi?dq=7821688"
driver = webdriver.Firefox()
driver.get(url)
driver.implicitly_wait(1)

price = driver.find_element(by= By.CLASS_NAME, value="price-box__price")

print(price.text)