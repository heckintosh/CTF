import sqlite3
import hashlib

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE users (
                  id INTEGER PRIMARY KEY,
                  username TEXT,
                  password TEXT)''')

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

username = "example_user"
password = "example_password"
hashed_password = hash_password(password)

cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))

conn.commit()
conn.close()
