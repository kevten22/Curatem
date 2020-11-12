from app import ma
from app.models.path_models import Path, Level, Course

class PathSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Path

class LevelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Level

class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course