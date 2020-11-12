from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from
from app import db
from app.routes import bp
from app.models.path_models import Path, Level, Course
from app.schemas.path_schemas import PathSchema, LevelSchema, CourseSchema

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
                        "name",
                        "category"
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
def createPath():
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
    Update a path by path id
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
    Delete a path by path id
    """
    try:
        if path_id is None:
            return "Please provide a valid path id", 401
        
        db.session.query(Level).filter(path = path_id).delete()
        db.session.query(Path).filter(id = path_id).delete()
        db.session.commit()

        return f"Path id {path_id} successfully deleted", 200

    except AttributeError:
        return 'There was an error with the database deleting this path', 400


@jwt_required
@bp.route('/path/level', methods=['POST'])
@swag_from({
        'tags': ['Levels'],
        'security': {
            'BasicAuth': []
        },
        'parameters': [{
                "name": "body",
                "in": "body",
                "required": "true",
                "schema": {
                    "id": "LevelSchema",
                    "required": [
                        "name",
                        "difficulty"
                    ],
                }
         }],
        'responses': {
            200: {
                'description': 'Success!',
                'schema': LevelSchema
            },
            400: {
                'description': 'Please provide a Name(string) and a Difficulty(string)'
            }
        }

}, validation=True)
def createLevel():
    """
    Create a level
    """
    try:
        body = request.json()
        level = Level(**body)
        db.session.add(level)
        db.session.commit()

        return 'Success!', 200

    except AttributeError:
        return 'Please provide a Name(string) and a Difficulty(string)', 400  

@jwt_required
@bp.route('/path/level/<int:path_id>', methods=['GET'])
@swag_from({
        'tags': ['Levels'],
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
                'description': 'A list of the levels that belong to the path id provided in the path',
                'schema': LevelSchema
            },
            401: {
                'description': 'Something went wrong in retrieving levels that belong to this path id'
            }
        }
})
def readPathLevels(path_id):
    """
    Get all levels that belong to a path
    """
    try:
        levels = db.session.query(Level).filter_by(path_id)

        return levels, 200
    
    except AttributeError:
        return 'Something went wrong in retrieving the levels that belong to this path id', 401

@jwt_required
@bp.route('/path/level/<int:level_id>', methods=['PUT'])
@swag_from({
        'tags': ['Levels'],
        'security': {
            'BasicAuth': []
        },
        'parameters': [{
                "name": "JWT Access Token",
                "in": "header",
                "required": "true",
         },
         {
                "name": "Level id",
                "in": "path",
                "type":"integer",
                "required": "true"
         },
         {
                "name": "body",
                "in": "body",
                "required": "true",
                "schema": {
                    "id": "LevelSchema",
                    "required": [
                        "name",
                        "difficulty",
                    ],
                }
         }],
        'responses': {
            200: {
                'description': 'An updated level will be returned',
                'schema': LevelSchema
            },
            400: {
                'description': 'Something went wrong in updating this level'
            }
        }

}, validation=True)
def updateLevel(level_id):
    """
    Update a level by level id
    """
    try:
        updated_level = request.json()
        path = db.session.query(Level).filter(id = level_id).update(updated_level)
        db.session.commit()

        return level, 200
    
    except AttributeError:
        return 'Something went wrong in updating this level', 400  

@jwt_required
@bp.route('/path/level/<int:level_id>', methods=['DELETE'])
@swag_from({
        'tags': ['Levels'],
        'security': {
            'BasicAuth': []
        },
        'parameters': [{
                "name": "JWT Access Token",
                "in": "header",
                "required": "true",
         },
         {
                "name": "Level id",
                "in": "path",
                "type":"integer",
                "required": "true"
         }],
        'responses': {
            200: {
                'description': 'Level successfully deleted'
            },
            400: {
                'description': 'Something went wrong deleting this level'
            }
        }

})
def deleteLevel(level_id):
    """
    Delete a level by level id
    """
    try:
        if level_id is None:
            return "Please provide a valid level id", 401

        path = db.session.query(Level).filter(id = level_id).delete()
        db.session.commit()

        return "Level successfully deleted", 200

    except AttributeError:
        return 'There was an error with the database deleting this path', 400    

@jwt_required
@bp.route('/path/level/course', methods=['POST'])
@swag_from({
        'tags': ['Courses'],
        'security': {
            'BasicAuth': []
        },
        'parameters': [
            {
                "name": "JWT Access Token",
                "in": "header",
                "required": "true",
            },
            {
                "name": "body",
                "in": "body",
                "required": "true",
                "schema": {
                    "id": "CourseSchema",
                    "required": [
                        "name",
                        "url"
                    ],
                }
         }],
        'responses': {
            200: {
                'description': 'Success!',
                'schema': CourseSchema
            },
            400: {
                'description': 'Please provide a Name(string) and a URL(string)'
            }
        }

}, validation=True)
def createCourse():
    """
    Create a course
    """
    try:
        body = request.json()
        course = Course(**body)
        db.session.add(course)
        db.session.commit()

        return 'Success!', 200

    except AttributeError:
        return 'Please provide a Name(string) and a URL(string)', 400

@jwt_required
@bp.route('/path/level/course/<int:level_id>', methods=['GET'])
@swag_from({
        'tags': ['Courses'],
        'security': {
            'BasicAuth': []
        },
        'parameters': [{
                "name": "JWT Access Token",
                "in": "header",
                "required": "true",
         },
         {
                "name": "Level id",
                "in": "path",
                "type":"integer",
                "required": "true"
         }],
        'responses': {
            200: {
                'description': 'A list of the courses that belong to the level id provided in the path',
                'schema': CourseSchema
            },
            400: {
                'description': 'Something went wrong in retrieving the courses that belong to this level id'
            }
        }
})
def readLevelCourses(level_id):
    """
    Get all courses that belong to a level
    """
    try:
        levels = db.session.query(Course).filter_by(level_id)

        return levels, 200
    
    except AttributeError:
        return 'Something went wrong in retrieving the courses that belong to this level id', 401

@jwt_required
@bp.route('/path/course/<int:path_id>', methods=['GET'])
@swag_from({
        'tags': ['Courses'],
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
                'description': 'A list of the courses that belong to the path id provided in the path',
                'schema': CourseSchema
            },
            400: {
                'description': 'Something went wrong in retrieving the courses that belong to this path id'
            }
        }
})
def readPathCourses(path_id):
    """
    Get all courses that belong to a path
    """
    try:

        levels = db.session.query(Level).filter_by(path_id)
        courses = db.session.query(Course).filter_by(levels)

        return courses, 200
    
    except AttributeError:
        return 'Something went wrong in retrieving the courses that belong to this path id', 401

@jwt_required
@bp.route('/path/level/course/<int:course_id>', methods=['PUT'])
@swag_from({
        'tags': ['Courses'],
        'security': {
            'BasicAuth': []
        },
        'parameters': [{
                "name": "JWT Access Token",
                "in": "header",
                "required": "true",
         },
         {
                "name": "Course id",
                "in": "path",
                "type":"integer",
                "required": "true"
         },
         {
                "name": "body",
                "in": "body",
                "required": "true",
                "schema": {
                    "id": "CourseSchema"
                }
         }],
        'responses': {
            200: {
                'description': 'An updated course will be returned',
                'schema': CourseSchema
            },
            401: {
                'description': 'Something went wrong in updating this course'
            }
        }

}, validation=True)
def updateCourse(course_id):
    """
    Update a course by course id
    """
    try:
        updated_course = request.json()
        path = db.session.query(course).filter(id = course_id).update(updated_course)
        db.session.commit()

        return level, 200
    
    except AttributeError:
        return 'Something went wrong in updating this course', 401

@jwt_required
@bp.route('/path/level/course/<int:course_id>', methods=['DELETE'])
@swag_from({
        'tags': ['Courses'],
        'security': {
            'BasicAuth': []
        },
        'parameters': [{
                "name": "JWT Access Token",
                "in": "header",
                "required": "true",
         },
         {
                "name": "Course id",
                "in": "path",
                "type":"integer",
                "required": "true"
         }],
        'responses': {
            200: {
                'description': 'Course successfully deleted'
            },
            400: {
                'description': 'Something went wrong deleting this course'
            }
        }

})
def deleteCourse(course_id):
    """
    Delete a course by course id
    """
    try:
        if course_id is None:
            return "Please provide a valid course id", 401

        path = db.session.query(Course).filter(id = course_id).delete()
        db.session.commit()

        return "Course successfully deleted", 200

    except AttributeError:
        return 'There was an error with the database deleting this course', 400