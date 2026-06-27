import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\rahma\OneDrive\Desktop\Rahm backup\L75\database.sqlite")

print("Opened data successfully")

# read SQL query for getting all the tables of database into a dataframe
tables = pd.read_sql("""SELECT * 
                     FROM sqlite_master
                     WHERE type='table';""", conn)

print(tables)
print()

# read table from the database into dataframe 
matches = pd.read_sql("""SELECT *
                      FROM Match;""", conn)

print(matches.head())
print()

# get the average win margin of all the winning teams for season 8
result1 = pd.read_sql("""SELECT AVG(Win_Margin), Match_Winner
                      FROM Match
                      WHERE Season_Id == 9
                      GROUP BY Match_Winner
                      ORDER BY AVG(Win_Margin);""",conn)
print(result1)
print()

# get the countt of the venues for season 9
result2 = pd.read_sql("""SELECT COUNT(DISTINCT Venue_Id)
                     FROM Match
                     WHERE Season_Id == 9;""",conn)
print(result2)
print()

#get the minimum, maximum, and average win margin 
# also get the total number of players who have recevied man of the match throughout all the seasons
result3= pd.read_sql("""SELECT MIN(Win_Margin), Max(Win_Margin), Avg(Win_Margin), COUNT(DISTINCT(Man_of_the_Match)) FROM Match;""", conn)
print(result3)
print()

# return total of win_margins for all the winners in season 9
result4 = pd.read_sql("""SELECT SUM(Win_Margin)
                      FROM Match
                      WHERE Season_Id == 9;""", conn)
print(result4)
