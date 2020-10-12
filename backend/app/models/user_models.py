from app import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User {self.name}>"