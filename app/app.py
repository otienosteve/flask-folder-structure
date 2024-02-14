from flask import Flask 
from flask_migrate import Migrate
from serializers import ma 

def create_app():
    app = Flask(__name__)
    from models import db 
    from route1 import route1_bp
    from route2  import route2_bp
    app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'
    app.config['SECRET_KEY'] = ''
    db.init_app(app) 
    ma.init_app(app)
    migrate = Migrate(app,db)
    app.register_blueprint(route1_bp)
    app.register_blueprint(route2_bp)

    return app