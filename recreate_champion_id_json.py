import requests
import json

# This code recreates champion_id.json with proper id - champion values, usefull in
# case if data gets corrupted or new champion gets released

version = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()[0]

url = f"http://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json"
response = requests.get(url)
response_json = response.json()["data"]
keys = response_json.values()

dicto = {}
for i in keys:
	dicto[i["key"]] = i["name"]

with open("champion_id.json", "w") as file:
	file.write(json.dumps(dicto))
