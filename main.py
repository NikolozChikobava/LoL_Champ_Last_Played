import requests
import json
import datetime


# Player in-game name
player_name = "RuStAvSkEe"

# eun1 for Eune, euw1 for Euw ...e
server = "eun1"

# Add your Api key
# UPDATE HERE /////////////////////////////////////////////////
api_key = None

if not api_key:
	raise ValueError("set your api_key from riot developer website")

url = f"https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{player_name}"
url = f"{url}?api_key={api_key}"

request = requests.get(url)
result_json = request.json()
# print(json.dumps(result_json, indent=2))
# Getting Encrypted ID from above api call

try:
	encrypted_id = result_json["id"]
except KeyError:
	raise ValueError("API_KEY is wrong -> Update & Set your API_KEY from riot developer website")

mastery_url = f"https://eun1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encrypted_id}"
mastery_url = f"{mastery_url}?api_key={api_key}"
mastery_request = requests.get(mastery_url)

# print(json.dumps(mastery_request.json(), indent=1))


mastery_json = mastery_request.json()
with open("champion_id.json", "r") as file:
	champion_id_name = json.load(file)

final_data = []
for i in mastery_json:
	last_time = datetime.datetime.fromtimestamp(i["lastPlayTime"] / 1000).strftime("%Y-%m-%d %H:%M:%S")
	final_data.append([champion_id_name[str(i["championId"])], last_time])

final_data.sort(key=lambda x: x[1])
print(player_name)
for i in final_data:
	print(f"{i[0]} {i[1]}")
