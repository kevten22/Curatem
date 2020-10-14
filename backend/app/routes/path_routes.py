from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.routes import bp
from app.models.path_models import Path

@jwt_required
@bp.route('/path', methods=['POST'])
def create():
    try:
        body = request.json()
        user = get_jwt_identity()
        path = Path(**body, user_id=user)
        db.session.add(path)
        db.session.commit()

        return 'Success!', 200

    except AttributeError:
        return 'Please provide a Name(string) and a Category(string)', 400

@jwt_required
@bp.route('/path/user', methods=['GET'])
def readUserPaths():
    try:
        user_id = get_jwt_identity()
        paths = db.session.query(Path).filter_by(user_id)

        return paths, 200
    
    except AttributeError:
        return 'Something went wrong in retrieving the user''s paths', 401

@bp.route('/path', methods=['GET'])
def readAllPaths():
    try:
        paths = db.session.query(Path)
        return paths, 200

    except AttributeError:
        return 'Something went wrong in retrieving all paths', 401

@jwt_required
@bp.route('/path/user/<int:path_id>', methods=['PUT'])
def updateUserPath(path_id):
    try:
        updated_path = request.json()
        path = db.session.query(Path).filter(Path.id = path_id).update(updated_path)
        db.session.commit()

        return path, 200
    
    except AttributeError:
        return 'Something went wrong in updating this path', 400

@jwt_required
@bp.route('/path/<int:path_id>', methods=['DELETE'])
def deletePath(path_id):
    try:
        if path_id is None:
            return "Please provide a valid path id", 401

        path = db.session.query(Path).filter(Path.id = path_id).delete()
        db.session.commit()

        return "Path successfully deleted", 200

    except AttributeError:
        return 'There was an error with the database deleting this path', 400

        

        