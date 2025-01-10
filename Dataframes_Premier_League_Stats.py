import pandas as pd

# Previously we have read the csv file, done some simple data analysis using the in-built csv module, and displayed some charts
# Now we create a dataframe which will allow us to summarise the data in an easily-readible manner, and perform calculations on it much more efficiently

# Load data and make sure column names are stripped off any trailing whitespaces
players = pd.read_csv('premier_league_player_stats.csv')
players.columns = players.columns.str.strip()

# Replace dashes with spaces in the club names
players["Club"] = players["Club"].str.replace("-", " ")

# Create a DataFrame with both the number of players and the top scorer with their goals in one step
club_player_counts_df = players.groupby("Club").agg(
    Number_of_players=("Name", "count"), # COLUMN 1: count number of players for each club
    Average_Age=("Age", lambda x: round(x.mean(), 1)), # COLUMN 2: calculate average age of squad, rounded to 1dp
    Top_Scorer=("Goals", lambda x: f"{players.loc[x.idxmax(), 'Name']} ({x.max()})"), # COLUMN 3: find top scorer of each club
    Top_Assists=("Assists", lambda x: f"{players.loc[x.idxmax(), 'Name']} ({x.max()})") # COLUMN 4: find top assistor of each club
).reset_index()

# Rename columns for clarity
club_player_counts_df.rename(columns={"Number_of_players": "No. of players",
                                      "Average_Age": "Average Age",
                                      "Top_Scorer": "Top Scorer (Total)", 
                                      "Top_Assists": "Most Assists (Total)"}, inplace=True)

# Display the DataFrame
print(club_player_counts_df)