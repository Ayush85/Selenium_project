import os
import xlsxwriter
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

os.environ['PATH'] = r'c:/SeleniumDrivers'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
action = ActionChains(driver)
driver.get('https://www.daraz.com.np/')
driver.implicitly_wait(5)

# ele = driver.find_element(By.CLASS_NAME, 'airship-html-prompt-shadow')
# shadow_root = driver.execute_script('return arguments[0].shadowRoot', ele)
# inner = shadow_root.find_element(By.CLASS_NAME, 'airship-alert-title').get_attribute('innerHTML').strip()
# print(inner)
catagory = driver.find_element(By.ID,'Level_1_Category_No1')
select_catagory = driver.find_element(By.CLASS_NAME,'lzd-site-menu-sub-item')
actions = ActionChains(driver)
actions.move_to_element(catagory)
actions.click(select_catagory)
actions.perform()
titles = driver.find_elements(By.CLASS_NAME,'c3e8SH')
result = []
for title in titles:
    name =  title.find_element(By.CLASS_NAME,'c3KeDq').get_attribute('textContent').strip()
    url = title.find_element(By.XPATH,'//div/div/div/div/div/a').get_attribute('href').strip()
    image =  title.find_element(By.XPATH,'//div/div/div/div/div/a/img').get_attribute('src').strip()
    price = title.find_element(By.CLASS_NAME,'c13VH6').get_attribute('textContent').strip()
    print(price)
    print(url)
    print(image)
    print(name)
    
driver.close()


