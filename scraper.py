from bs4 import BeautifulSoup
from selenium import webdriver
import os

edhrec_card_page = input("Please input the link from edhrec here! : ")

deck_name = edhrec_card_page.split("/")[4]

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/Users/seanmcquaid/development/chrome-selenium/chromedriver", options=options)

driver.get(edhrec_card_page)
driver.implicitly_wait(100)

page = driver.page_source

soup = BeautifulSoup(page, "html.parser")

cards = soup.findAll("div", {"class" : "nwname"})


def create_deck_list_file(card_list):
    file_name = deck_name + ".txt"
    file = open(file_name , "w+")
    for card in card_list:
        file.write(card.text + "\n")
    file.close()

create_deck_list_file(cards)