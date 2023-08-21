import requests
import json

f =  open("data_to_get_started.json") 
json_data = json.load(f)

premier_league_id= json_data["league_ids"]["premier_league"]

f = open("credentials.json") 
json_data_creds = json.load(f)

rapid_api_key = json_data_creds["api_keys"]["rapidapi_api_key"]


print("starting api code")

#get all team ids from premier league
url = "https://api-football-v1.p.rapidapi.com/v3/teams"
headers = {
	"X-RapidAPI-Key": rapid_api_key,
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

params = {
	"league": premier_league_id,
	"season":2023
}

response = requests.get(url = url, headers=headers, params=params)
print(response)
print(response.text)
json_data = response.json()

with open("team_data.json", "w") as f:
    json.dump(json_data, f)

print("completed api code")

