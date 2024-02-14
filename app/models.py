from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

def generate_uuid():
    return str(uuid.uuid4())

class User(db.Model):
    __tablename__ ='users'
    id = db.Column(db.String,primary_key=True,default=generate_uuid)