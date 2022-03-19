from itertools import count
import os
from typing import Counter
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
results = []
def scrap_item_url():
    titles = driver.find_elements(By.XPATH,'//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div[2]/a')
    urls = []
    for title in titles:
        url = title.get_attribute('href')
        urls.append(url)
        print(url)
    results.append(urls)

catagory = driver.find_element(By.ID,'Level_1_Category_No1')
select_catagory = driver.find_element(By.XPATH,'//*[@id="J_8018372580"]/div/ul/ul[1]/li[1]')
actions = ActionChains(driver)
actions.move_to_element(catagory)
actions.click(select_catagory)
actions.perform()
urls = []
count = 1
next_page = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[3]/div/ul/li[9]')
while(next_page.get_attribute('aria-disabled')!='true'):
    
    scrap_item_url()
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print(next_page.get_attribute('aria-disabled')+'and' + str(count))
    actions.click(next_page)
    actions.perform()
    count = count+1
    time.sleep(0.5)
driver.close()
# print(urls)
for url in results:
    for u in url:
        print(u)