from app import ma
from app.models.path_models import Path, Level

class PathSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Path

class LevelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Level