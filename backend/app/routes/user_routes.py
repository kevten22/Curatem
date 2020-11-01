from flask import current_app as app, request, jsonify
from flask_jwt_extended import create_access_token
from flasgger import swag_from
from app import db
from app.routes import bp
from app.models.user_models import User
from app.schemas.user_schemas import UserSchema
import datetime

@bp.route('/user/register', methods=['POST'])
@swag_from({
        'tags': ['Users'],
        'parameters': [{
                "name": "body",
                "in": "body",
                "required": "true",
                "schema": {
                    "id": "UserSchema",
                    "required": [
                        "email",
                        "username",
                        "password"
                    ],
                }
         }],
        'responses': {
            200: {
                'description': 'Success',
            }
        }
}, validation=True)
def register():
    """
    This route is used for registering a user and receiving an access token in return
    """
    try:
        email = request.json.get('email', None)
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        user = User(email=email, username=username,password=password)
        db.session.add(user)
        db.session.commit()

        return 'Success', 200

    except AttributeError:
        return 'Provide a Username and Password in JSON format in the request body', 400

@bp.route('/user/login', methods=['POST'])
@swag_from({
    "tags": ['Users'],
    'parameters': [{
            "name": "email",
            "in": "path",
            "type": "string",
            "required": "true",
            "description": "The user's email address."
        },
        {
            "name": "password",
            "in": "path",
            "type": "string",
            "required": "true",
            "description": "The user's password."
        }],
    'responses': {
            200: {
                'description': 'An access token for the user to log in with',
            }
        }

})
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