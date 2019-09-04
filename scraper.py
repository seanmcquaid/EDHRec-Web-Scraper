import requests
from bs4 import BeautifulSoup
from selenium import webdriver

base_url = "https://edhrec.com/commanders/arcades-the-strategist"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/Users/seanmcquaid/development/chrome-selenium/chromedriver", chrome_options=options)

driver.get(base_url)
driver.implicitly_wait(100)

page = driver.page_source

soup = BeautifulSoup(page, "html.parser")

cards = soup.findAll("div", {"class" : "nwname"})

names = []

for card in cards:
    print(card.text)