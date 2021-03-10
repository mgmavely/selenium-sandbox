from selenium import webdriver

chrome_driver_path = "C:\\Users\\mgmma\\Desktop\\Python Projects\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
list_items = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
dates = [i.text for i in list_items.find_elements_by_tag_name('time')]
events = [i.text for i in list_items.find_elements_by_tag_name('a')]

formatted_dict = {i: {'time': dates[i], 'name': events[i]} for i in range(5)}

print(formatted_dict)
driver.close()
