from flask import current_app as app, request
from flask_jwt_extended import create_access_token
from app import db
from app.routes import bp
from app.models.user_models import User
import datetime

@bp.route('/user/register', methods=['POST'])
def register():
    try:
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        user = User(username=username,password=password)
        db.session.add(user)
        db.session.commit()

        return 'Success', 200

    except AttributeError:
        return 'Provide a Username and Password in JSON format in the request body', 400

@bp.route('/user/login', methods=['POST'])
def login():
    try:
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        user = User.query.filter_by(username=username).first()

        authorized = user.check_password(password)

        if not authorized:
            return {'error': "Wrong email or password"}, 401

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)

        return {'token': access_token}, 200


    except AttributeError:
        return 'Provide a Username and Password in JSON format in the request body', 400