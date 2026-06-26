import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\rahma\OneDrive\Desktop\Rahm backup\L74\database.sqlite")

print("Opened data successfully")
print()

# Read SQL query for getting all the tables of database into a dataframe
tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""", conn)
print(tables)
print()

# check team id of all teams
teams = pd.read_sql("""SELECT * FROM Team;""", conn)
print(teams)
print()

#read table from the database into dataframe 
matches = pd.read_sql("""SELECT * FROM Match;""", conn)

print(matches)
print()

#check details of all the matches won by Mumbai Indians
MI_wins = pd.read_sql("""SELECT * FROM Match WHERE Match_Winner == 7;""", conn)
print(MI_wins)
print()

#check the details of alll the matches won by Mumabai Indians in the last two seasons
MI_S8_S9 = pd.read_sql("""SELECT * FROM Match WHERE Match_Winner == 7 and Season_Id IN (8,9);""", conn)
print(MI_S8_S9)
print()

new_teams = pd.read_sql("""SELECT *
                        FROM Team
                        WHERE Team_Name LIKE 'De%';""",conn)
print(new_teams)
print()

# Check the minimum and maximum win_margin of all the matches 
min_max_margin = pd.read_sql("""SELECT MIN(Win_Margin), MAX(Win_Margin) FROM Match;""", conn)
print(min_max_margin)
