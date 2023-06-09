from time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:/Users/karth/OneDrive/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://ineuron.ai/category/DATA-SCIENCE")
time.sleep(1)

driver.find_element(by=By.XPATH,value='//*[@id="__next"]/div[5]/div/div[2]/div/div/div/div[1]/div').click()
driver.find_element(by=By.XPATH,value=)