import sqlite3
import hashlib

conn = sqlite3.connect('database_toBeFinished.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE users (
                  id INTEGER PRIMARY KEY,
                  password TEXT,
                  username TEXT)''')

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

username = "admin"
password = "password"
hashed_password = hash_password(password)

cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))

conn.commit()
conn.close()
