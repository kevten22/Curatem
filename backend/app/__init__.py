from flask import Flask, request
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevelopmentConfig')
    db.init_app(app)
    bcrypt.init_app(app)
    migrate = Migrate(app, db)
    
    with app.app_context():
        db.create_all()

        from app.models import bp as models_bp
        app.register_blueprint(models_bp)

        from app.routes import bp as routes_bp
        app.register_blueprint(routes_bp)

    return app  
