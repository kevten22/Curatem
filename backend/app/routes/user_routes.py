from flask import current_app as app
from app import db
from app.routes import bp

@bp.route('/register', methods=['POST'])
def register():
    try:
        username = request.json.get('userna
        me', None)
        password = request.json.get('password', None)

        user = User(username=username,password=password)
        db.session.add(user)
        db.session.commit()

        return'success', 200

    except AttributeError:
        return 'Provide a Username and Password in JSON format in the request body', 400