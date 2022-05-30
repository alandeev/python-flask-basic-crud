from dataclasses import dataclass
from app import Flask
from flask_sqlalchemy import SQLAlchemy

server = Flask(__name__)
db = SQLAlchemy(server)

@dataclass
class UserModel(db.Model):
  __tablename__ = "user"

  id: str 
  username: str

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(200), unique=True)

@dataclass
class TaskModel(db.Model):
  __tablename__ = "task"

  id: str
  title: str
  description: str
  status: str

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255))
  description = db.Column(db.String(255))
  status = db.Column(db.String(50))
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
