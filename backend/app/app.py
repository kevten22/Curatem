from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import bcrypt
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres123@localhost:5433/Curatem"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.name}>"

@app.route('/register', methods=['POST'])
def register():
    try:
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        user = User(username=username,password=password)
        db.session.add(user)
        db.session.commit()

        return'success', 200

    except AttributeError:
        return 'Provide a Username and Password in JSON format in the request body', 400

@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()