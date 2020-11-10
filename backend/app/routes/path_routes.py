from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from
from app import db
from app.routes import bp
from app.models.path_models import Path
from app.schemas.path_schemas import PathSchema

@jwt_required
@bp.route('/path', methods=['POST'])
@swag_from({
        'tags': ['Paths'],
        'security': {
            'BasicAuth': []
        },
        'parameters': [{
                "name": "body",
                "in": "body",
                "required": "true",
                "schema": {
                    "id": "PathSchema",
                    "required": [
                        
                    ],
                }
         }],
        'responses': {
            200: {
                'description': 'Success!',
                'schema': PathSchema
            },
            400: {
                'description': 'Please provide a Name(string) and a Category(string)'
            }
        }

}, validation=True)
def create():
    """
    Create a path
    """
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
@swag_from({
        'tags': ['Paths'],
        'security': {
            'BasicAuth': []
        },
        'parameters': [{
                "name": "JWT Access Token",
                "in": "header",
                "required": "true",
         }],
        'responses': {
            200: {
                'description': 'A list of the paths for the user with the id being grabbed from the access token',
                'schema': PathSchema
            },
            400: {
                'description': 'Something went wrong in retrieving the user''s paths'
            }
        }

})
def readUserPaths():
    """
    Get all paths that belong to a user
    """
    try:
        user_id = get_jwt_identity()
        paths = db.session.query(Path).filter_by(user_id)

        return paths, 200
    
    except AttributeError:
        return 'Something went wrong in retrieving the user''s paths', 401

@bp.route('/path', methods=['GET'])
@swag_from({
        'tags': ['Paths'],
        
        'responses': {
            200: {
                'description': 'A list of every path ever created.',
                'schema': PathSchema
            },
            400: {
                'description': 'Something went wrong in retrieving all the paths'
            }
        }

})
def readAllPaths():
    """
    Get all paths.  This will probably be deprecated as the data scales
    """
    try:
        paths = db.session.query(Path)
        return paths, 200

    except AttributeError:
        return 'Something went wrong in retrieving all paths', 401

@jwt_required
@bp.route('/path/user/<int:path_id>', methods=['PUT'])
@swag_from({
        'tags': ['Paths'],
        'security': {
            'BasicAuth': []
        },
        'parameters': [{
                "name": "JWT Access Token",
                "in": "header",
                "required": "true",
         },
         {
                "name": "Path id",
                "in": "path",
                "type":"integer",
                "required": "true"
         },
         {
                "name": "body",
                "in": "body",
                "required": "true",
                "schema": {
                    "id": "PathSchema",
                    "required": [
                        "name",
                        "category",
                    ],
                }
         }],
        'responses': {
            200: {
                'description': 'An updated path will be returned',
                'schema': PathSchema
            },
            400: {
                'description': 'Something went wrong in updating this path'
            }
        }

}, validation=True)
def updateUserPath(path_id):
    """
    Update a path using by path id
    """
    try:
        updated_path = request.json()
        path = db.session.query(Path).filter(id = path_id).update(updated_path)
        db.session.commit()

        return path, 200
    
    except AttributeError:
        return 'Something went wrong in updating this path', 400

@jwt_required
@bp.route('/path/<int:path_id>', methods=['DELETE'])
@swag_from({
        'tags': ['Paths'],
        'security': {
            'BasicAuth': []
        },
        'parameters': [{
                "name": "JWT Access Token",
                "in": "header",
                "required": "true",
         },
         {
                "name": "Path id",
                "in": "path",
                "type":"integer",
                "required": "true"
         }],
        'responses': {
            200: {
                'description': 'Path successfully deleted'
            },
            400: {
                'description': 'Something went wrong deleting this path'
            }
        }

})
def deletePath(path_id):
    """
    Delete an path by path id
    """
    try:
        if path_id is None:
            return "Please provide a valid path id", 401

        path = db.session.query(Path).filter(id = path_id).delete()
        db.session.commit()

        return "Path successfully deleted", 200

    except AttributeError:
        return 'There was an error with the database deleting this path', 400

        

        