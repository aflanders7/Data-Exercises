import requests
import csv

url = "https://statsapi.mlb.com/api/v1/stats?stats=season&group=pitching&playerPool=all&season=2018&teamId=144"
response = requests.get(url)
data = response.json()
stats = data.get("stats")
splits = stats[0]["splits"]

csv_file = "player_stats.csv"

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
        "playerId", "playerName", "gamesPitched", "strikes", "singles", "doubles", "triples", "homeRuns", "hits", "outs", "strikeOuts"
    ])

    for player in splits:
            player_stat = player["stat"]
            name = player["player"]["lastName"] + ", " + player["player"]["firstName"]
            singles = player_stat["hits"] - player_stat["doubles"] - player_stat["triples"] - player_stat["homeRuns"]
            outs = player_stat["strikeOuts"] + player_stat["groundOuts"] + player_stat["airOuts"]

            writer.writerow([
                player["player"]["id"],
                name,
                player_stat["gamesPitched"], 
                player_stat["strikes"], 
                singles, 
                player_stat["doubles"],
                player_stat["triples"],
                player_stat["homeRuns"],
                player_stat["hits"],
                outs,
                player_stat["strikeOuts"]
            ])
