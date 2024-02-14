from flask import Blueprint 

route2_bp = Blueprint('route1',__name__)

@route2_bp.route('/')
def home():
    return "route 2"