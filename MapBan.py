from bs4 import BeautifulSoup
import requests

url = 'https://overwatch.blizzard.com/en-us/rates/?input=PC&map=all-maps&region=Americas&role=All&rq=1&tier=All'
source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')

winrates = {}

for span in soup.find_all(class_="percent-value"):
    hero_id = span.get("id")
    if hero_id and hero_id.endswith("-winrate-value"):
        hero_name = hero_id.replace("-winrate-value", "")
        if span.text == '--':
            continue
        percent = float(span.text.strip('%'))
        winrates[hero_name] = percent

print(winrates)