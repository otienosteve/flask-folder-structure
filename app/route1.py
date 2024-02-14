from flask import Blueprint 

route1_bp = Blueprint('route1',__name__)

@route1_bp.route('/')
def home():
    return "route 1"