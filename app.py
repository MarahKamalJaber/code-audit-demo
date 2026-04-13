
import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

user_input = input("Enter username: ")

# ❌ Vulnerable query (SQL Injection)
query = "SELECT * FROM users WHERE name = '" + user_input + "'"

cursor.execute(query)
print("Query executed!")
