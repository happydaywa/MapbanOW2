from bs4 import BeautifulSoup
import requests

DesiredHero = input("What is your desired hero: ").strip().lower().replace(" ", "-")

Maps = {}
for i in range(1, 4):
    map_name = input(f"Map {i}: ").strip().lower().replace(" ", "-")
    Maps[f"Map{i}"] = map_name

for map_key, map_name in Maps.items():
    url = f'https://overwatch.blizzard.com/en-us/rates/?input=PC&map={map_name}&region=Americas&role=All&rq=1&tier=All'
    
    try:
        source = requests.get(url).text
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {map_name}: {e}")
        continue

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

    if DesiredHero in winrates:
        print(f"{DesiredHero} winrate: {winrates[DesiredHero]} in {map_name}")
    else:
        print(f"Hero {DesiredHero} not recognized on {map_name}.")

# print(winrates)


