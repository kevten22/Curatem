from app import ma
from app.models.user_models import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True