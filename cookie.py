from selenium import webdriver
import time

chrome_driver_path = "C:\\Users\\mgmma\\Desktop\\Python Projects\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_css_selector("#bigCookie")


def click_cookie():
    for i in range(100):
        cookie.click()


def upgrade():
    upgrades_tab = driver.find_element_by_css_selector("#upgrades")
    upgrades_list = upgrades_tab.find_elements_by_css_selector(".enabled")
    products_tab = driver.find_element_by_css_selector("#products")
    products_list = products_tab.find_elements_by_css_selector(".enabled")
    if len(upgrades_list) != 0:
        upgrades_list[-1].click()
    elif len(products_list) != 0:
        products_list[-1].click()


while True:
    click_cookie()
    upgrade()
