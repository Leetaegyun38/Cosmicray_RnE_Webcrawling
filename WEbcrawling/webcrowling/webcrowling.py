
from selenium import webdriver
import datetime
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(1)
driver.get('https://minjoos.tistory.com/')