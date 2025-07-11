from sqlite3.dbapi2 import Cursor
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
db = 'users.db'

def searchdb(username, password):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    if username and password in cursor.fetchall():
        conn.close()
        return True
    else:
        conn.close()
        return False

@app.route('/login/', methods=['GET', 'POST'])
def login():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL, password TEXT NOT NULL);')
    if request.method == 'POST':
        action = request.form['action']
        username = request.form['username']
        password = request.form['password']
        if action == 'register':
            cursor.execute('INSERT INTO users (user, senha), VALUES(?, ?)', username, password)
        elif action == 'login':
            if searchdb(username, password) == True:
                return 'Logado com sucesso!'
            else:
                return 'Você tem que criar registrar o usuário'
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
