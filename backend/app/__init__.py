from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres123@localhost:5433/Curatem"
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()

    return app
