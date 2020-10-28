from app import db
from flask_bcrypt import generate_password_hash, check_password_hash


followers_table = db.Table('followers', db.Model.metadata, 
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('path_id', db.Integer, db.ForeignKey('paths.id'))
)

paths_completed_table = db.Table('paths_completed', db.Model.metadata, 
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('path_id', db.Integer, db.ForeignKey('paths.id'))
)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    email = db.Column(db.String())
    paths_followed = db.relationship('Path', secondary=followers_table)
    paths_created = db.relationship('Path', backref='creator', lazy=True)
    paths_completed = db.relationship('Path', secondary=paths_completed_table)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User {self.name}>"

