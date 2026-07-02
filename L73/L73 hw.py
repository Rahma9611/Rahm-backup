import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\rahma\OneDrive\Desktop\Rahm backup\L73\L73 database.sqlite")
print("Opended data successfully ")

tables = pd.read_sql("SELECT * FROM sqlite_master WHERE type='table';", conn)
print(tables)