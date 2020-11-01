from flask import current_app as app, request, jsonify
from flask_jwt_extended import create_access_token
from flasgger import swag_from
from app import db
from app.routes import bp
from app.models.user_models import User
from app.schemas.user_schemas import UserSchema
import datetime

@bp.route('/user', methods=['GET'])
@swag_from({
        'responses': {
            200: {
                'description': 'This is the schema for the User model',
                'schema': UserSchema
            }
        }
})
def documentation():
    """
    Hello
    """
    result = 'hi'
    return jsonify(result)

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