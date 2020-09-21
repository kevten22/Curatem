from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres123@localhost:5433/Curatem"
    db.init_app(app)
    migrate = Migrate(app, db)

    from app.models import bp as models_bp
    app.register_blueprint(models_bp)

    from app.models import bp as routes_bp
    app.register_blueprint(routes_bp)

    with app.app_context():
        db.create_all()

    return app  
