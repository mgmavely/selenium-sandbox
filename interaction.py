from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\\Users\\mgmma\\Desktop\\Python Projects\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

search = driver.find_element_by_name('fName')
search.send_keys('Michael')
search = driver.find_element_by_name('lName')
search.send_keys('Mavely')
search = driver.find_element_by_name('email')
search.send_keys('m@mail.com')
driver.find_element_by_class_name("btn").click()
