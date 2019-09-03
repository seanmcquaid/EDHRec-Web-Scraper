import requests
from bs4 import BeautifulSoup

base_url = "https://edhrec.com/commanders/arcades-the-strategist-wall-tribal"

page = requests.get(base_url)

soup = BeautifulSoup(page.text, "html.parser")

cards = soup.find_all("div", class_= "cards")

print(cards)

x = 0

for x in cards:
    print(x.getText())