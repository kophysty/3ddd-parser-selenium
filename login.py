from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome(executable_path='driver\\chromedriver.exe')

driver.get('https://3ddd.ru/login')

input('Напишите "y", когда залогинитесь')

