import os
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

os.environ['PATH'] = r"c:/SeleniumDrivers"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
action = ActionChains(driver)
driver.get('https://www.daraz.com.np/')
driver.implicitly_wait(50)

catagory = driver.find_element(By.ID,'Level_1_Category_No1')
select_catagory = driver.find_element(By.XPATH,'//*[@id="J_8018372580"]/div/ul/ul[1]/li[1]')
actions = ActionChains(driver)
actions.move_to_element(catagory)
actions.click(select_catagory)
actions.perform()
titles = driver.find_elements(By.XPATH,'//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div[2]/a')
urls = []
results = []
for title in titles:
    url = title.get_attribute('href')
    urls.append(url)
    print(url)
print(urls)
for url in urls:
    driver.get(str(url))
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    height = driver.execute_script("return document.body.scrollHeight")
    for i in range(int(height)):
        driver.execute_script('window.scrollBy(0,1)') # scroll by 20 on each iteration
        height = driver.execute_script("return document.body.scrollHeight") # reset height to the new height after scroll-triggered elements have been loaded.
    name =  driver.find_element(By.XPATH,'//*[@id="module_product_title_1"]/div/div/span').text
    print(name)
    image =  driver.find_element(By.XPATH,'//*[@id="module_item_gallery_1"]/div/div/div/img').get_attribute('src').strip()
    print(image)
    price = driver.find_element(By.XPATH,'//*[@id="module_product_price_1"]/div/div/span').text
    print(price)
    descriptions = driver.find_element(By.XPATH,'//*[@id="module_product_detail"]/div/div/div/div/ul').text
    print(descriptions)
    rating = driver.find_element(By.XPATH,'//*[@id="module_product_review"]/div/div/div/div/div/div/div').text
    print(rating)
    results.append([name,price,image,rating, descriptions, url])
driver.close()
print(results)
data = pd.DataFrame(results)
data.columns = ['name', 'price', 'image', 'rating', 'descriptions','url']
data.to_csv('results.csv', index=False)
    


