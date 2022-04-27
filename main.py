import httpx
import json

url = "https://api.sofascore.com/api/v1/sport/football/events/live"
headers = {
    "authority": "api.sofascore.com",
    "accept": "*/*",
    "accept-language": "ru,en-US;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "dnt": "1",
    "if-none-match": "W/^\^01c21b3c5e^^",
    "origin": "https://www.sofascore.com",
    "referer": "https://www.sofascore.com/",
    "sec-ch-ua": "^\^Chromium^^;v=^\^100^^, ^\^",
}
response = httpx.request("GET", url, headers=headers)
jsondata = json.loads(response.text)

with open("scores.json", "w", encoding="utf-8") as f:
    json.dump(jsondata, f, ensure_ascii=False, indent=4)

for event in jsondata["events"]:
    tournament = event["tournament"]["name"]
    hometeam = event["homeTeam"]["name"]
    awayteam = event["awayTeam"]["name"]
    homescore = event["homeScore"]["current"]
    awayscore = event["awayScore"]["current"]
    print(f"{tournament} | {hometeam} {homescore} - {awayscore} {awayteam}")
