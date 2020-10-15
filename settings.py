from flask import Flask

app = Flask(__name__)
# insert path below
MY_PATH = "your/path/to/flask-to-do-list"

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{MY_PATH}/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
