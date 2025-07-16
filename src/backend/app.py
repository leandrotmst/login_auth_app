from flask import Flask, render_template, request
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)')
    conn.commit()
    conn.close()

init_db()

def register(username: str, password: str):
    hashed_password = generate_password_hash(password)
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    conn.close()

def search(username: str, password: str):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT password FROM users WHERE username = ?', (username,))
    row = c.fetchone()
    conn.close()
    if row and check_password_hash(row[0], password):
        return True
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form['action']
        username = request.form['username']
        password = request.form['password']

        if action == 'register':
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute('SELECT username FROM users WHERE username = ?', (username,))
            exists = c.fetchone()
            conn.close()
            if not exists:
                register(username, password)
            else:
                return render_template('index.html', message='Usuário já existe, pode fazer o login')

        if action == 'login':
            if search(username, password):
                return render_template('success.html')
            else:
                return render_template('error.html')

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)