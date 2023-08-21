import requests
import json

f =  open("data_to_get_started.json") 
json_data = json.load(f)

premier_league_id= json_data["league_ids"]["premier_league"])

f = open("credentials.json") 
json_data_creds = json.load(f)

rapid_api_key = json_data_creds["api_keys"]["rapidapi_api_key"]



#get all team ids from premier league
url
headers = {
	"X-RapidAPI-Key": rapid_api_key,
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

params = {
	"league" = str(premier_league_id)
}

response = requests.get(url, headers=headers, params=params)

