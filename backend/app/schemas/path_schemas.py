from app import ma
from app.models.path_models import Path

class PathSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Path
        include_fk = True