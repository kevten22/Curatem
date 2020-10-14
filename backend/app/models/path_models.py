from app import db

class Path(db.Model):
    __tablename__ = 'paths'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    category = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    
