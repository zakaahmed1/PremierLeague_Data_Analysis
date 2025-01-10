# the dataset used is player statistics of Premier League players active in 2020 (see premier_league_player_stats.csv)
# make sure the premier_league_player_stats.csv file is located in the same folder as this Python code when running it

import csv
from collections import namedtuple

Player = namedtuple("Player", "name club position appearances goals goals_per_match assists")

players = []

with open("premier_league_player_stats.csv", "r", encoding = 'utf-8') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader) # skips the header
    # I only want the relevant columns mentioned above when defining Player
    for row in reader:
        new_player = {}
        new_player["name"] = row[0]
        new_player["club"] = row[2]
        new_player["position"] = row[3]
        new_player["appearances"] = row[6]
        new_player["goals"] = row[9]
        new_player["goals_per_match"] = row[10]
        new_player["assists"] = row[39]
        players.append(new_player)

# We don't care about players with 0 appearances, so we remove them:

filtered_players = []

for player in players:
    if int(player["appearances"]) != 0:
        filtered_players.append(player)

# Which active player in 2020 has scored the most Premier League goals

player_with_most_goals = filtered_players[0]

for player in filtered_players:
    if int(player["goals"]) > int(player_with_most_goals["goals"]):
        player_with_most_goals = player

print(f"The player with the most goals in the Premier League is {player_with_most_goals["name"]} with {player_with_most_goals["goals"]}.")

# Find all the Manchester United players. What is their average number of appearances

total_appearances = 0
number_of_players = 0

for player in filtered_players:
    if player["club"] == "Manchester-United":
        total_appearances += int(player["appearances"])
        number_of_players += 1

average_appearances = total_appearances / number_of_players

print(f"The average number of appearances per Manchester United player is {average_appearances}")

# What is the average number of goals scored for Arsenal forwards

total_goals = 0
number_of_arsenal_forwards = 0

for player in filtered_players:
    if player["club"] == "Arsenal" and player["position"] == "Forward":
        total_goals += int(player["goals"])
        number_of_arsenal_forwards += 1

average_goals = total_goals / number_of_arsenal_forwards

print(f"The average number of goals per Arsenal forward is {average_goals:.2f}")