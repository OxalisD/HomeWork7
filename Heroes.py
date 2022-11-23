import requests

heroes = {"Hulk": {}, "Captain America": {}, "Thanos": {}}
base = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/"

responce = requests.get(base + "all.json")
for hero in responce.json():
    name = hero["name"]
    if name in list(heroes.keys()):
        heroes[name]["id"] = hero["id"]

for hero in heroes.keys():
    powerstats = requests.get(base + "powerstats/" + str(heroes[hero]["id"]) + ".json")
    heroes[hero]["intelligence"] = powerstats.json()["intelligence"]

print(f"Самый умный герой: {max(heroes.items(), key=lambda x: x[1]['intelligence'])[0]}")

