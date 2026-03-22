import pandas as pd
import sqlite3
import os
print(os.getcwd())

# load csv dataset
df = pd.read_csv(r"C:/Users/Shravya/OneDrive - Malla Reddy Engineering College for Women/Desktop/apexxx/TASK 2/data/sales_data.csv")

# create database
conn = sqlite3.connect("superstore.db")

# convert csv into sql table
df.to_sql("superstore", conn, if_exists="replace", index=False)

print("Data imported successfully!")

conn.close()
