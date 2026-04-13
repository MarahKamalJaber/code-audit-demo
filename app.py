import sqlite3

def login():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    username = input("Enter username: ")
    password = input("Enter password: ")

    # ❌ SQL Injection vulnerability
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        print("Login success")
    else:
        print("Login failed")

login()
