from flask import Blueprint

bp = Blueprint('routes', __name__, url_prefix='/routes')

from app.routes import user_routes