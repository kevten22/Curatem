from flask import Flask, request
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flasgger import Swagger

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()
ma = Marshmallow()
swag = Swagger()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevelopmentConfig')
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    swag.init_app(app)
    app.config['SWAGGER'] = {
        'title': 'Curatem Backend API',
    }
    
    with app.app_context():

        from app.models import bp as models_bp
        app.register_blueprint(models_bp)

        from app.routes import bp as routes_bp
        app.register_blueprint(routes_bp)

    return app  
