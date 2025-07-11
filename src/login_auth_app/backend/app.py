from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
db = 'users.db'

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

def initdb():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE users IF NOT EXISTS (username TEXT NOT NULL, password_hash TEXT NOT NULL);')
    conn.close()

def insertdb(values: list[str]):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password_hash) VALUES', values)
    conn.commit()
    conn.close()

def searchdb(username: str, password: str):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password_hash = ?', (username, password))
    results = cursor.fetchall()
    conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
