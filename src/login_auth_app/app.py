import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)
db = "users.db"


@app.route("/", methods=["GET", "POST"])
def login():
    if request.form == "POST":
        username = request.form["username"]
        password = request.form["password"]
        action = request.form["action"]
        if action == "register":
            searchdb(username, password)
            if searchdb(username, password) == None:
                values = [username, password]
                insertdb(values)
            if searchdb(username, password) != None:
                return render_template("user_exists.html")

        elif action == "login":
            searchdb(username, password)
            if searchdb(username, password) == None:
                return render_template("register.html")
            return render_template("login_sucess.html")

    return render_template("login.html")


def initdb():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE users IF NOT EXISTS (username TEXT NOT NULL, password_hash TEXT NOT NULL);"
    )
    conn.close()


def insertdb(values: list[str]):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password_hash) VALUES", values)
    conn.commit()
    conn.close()


def searchdb(username: str, password: str):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password_hash = ?",
        (username, password),
    )
    search = cursor.fetchone()
    conn.close()
    return search


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
