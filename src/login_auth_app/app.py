from flask import Flask, render_template
# Flask
# https://flask.palletsprojects.com/en/latest/

# Flask-SQLAlchemy
# https://docs.sqlalchemy.org/en/latest/

# SQLAlchemy
# https://docs.sqlalchemy.org/en/latest/

# Flask-Login
# https://flask-login.readthedocs.io/en/latest/

# Flask Migrate
# https://flask-migrate.readthedocs.io/en/latest/

# Flask e banco de dados
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

# Real Python
# https://realpython.com/

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("login.html")

if __name__ == '__main__':
    index()
