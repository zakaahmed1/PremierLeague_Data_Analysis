import pandas as pd
import matplotlib.pyplot as plt

# Load data and strip column names of trailing whitespaces
players = pd.read_csv('premier_league_player_stats.csv')
players.columns = players.columns.str.strip()

# We want to create a bar chart to show the Premier League players with the most goals per match.
# Filter players with over 50 appearances to avoid outliers who may have played 1 game and scored 1 goal - an unnatural trend
players_over_50_appearances = players[players["Appearances"] > 50]

# Bar chart data for top 10 players with the most goals per match, using the 'head' method to display the first 10 results after sorting
top_10_goals_per_match = players_over_50_appearances.sort_values("Goals per match", ascending=False).head(10)

# Pie chart data for player distribution by position (percentage of players who play at each position)
position_distribution = players["Position"].value_counts()

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Extract last names for the bar plot, for better readability
last_names = top_10_goals_per_match["Name"].apply(lambda x: x.split()[-1])

# Bar plot on the left
axes[0].bar(
    last_names,
    top_10_goals_per_match["Goals per match"],
    color="maroon",
    width=0.75
)
axes[0].set_xlabel("Player Last Name")
axes[0].set_ylabel("Goals per Match")
axes[0].set_title("Top 10 Players with Highest Goals per Match (Over 50 Appearances)")
axes[0].tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better readability

# Pie chart on the right
axes[1].pie(
    position_distribution.values,
    labels=position_distribution.index,
    autopct="%1.1f%%",
)
axes[1].set_title("Distribution of Players by Position")

# Adjust layout and display
plt.tight_layout() # makes sure the subplots do not overlap
plt.show()