from app import db

class Path(db.Model):
    __tablename__ = 'paths'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    category = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    followers = db.relationship('User', secondary="followers")
    users_completed = db.relationship('User', secondary="paths_completed")
    levels = db.relationship('Level')
    
class Level(db.Model):
    __tablename__ = 'levels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    difficulty = db.Column(db.String())
    path = db.Column(db.Integer, db.ForeignKey('paths.id'))
    following_level = db.Column(db.Integer, db.ForeignKey('levels.id'))
