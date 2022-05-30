from dataclasses import dataclass
from app import Flask
from flask_sqlalchemy import SQLAlchemy
 
server = Flask(__name__)
db = SQLAlchemy(server)
 
@dataclass
class UserModel(db.Model):
    id: int
    email: str

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)