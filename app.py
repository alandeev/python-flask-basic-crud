from flask import Flask, render_template, request, redirect, jsonify
from sqlalchemy import null
from models import db, UserModel
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()
 
@app.post("/users")
def create():
  email = request.json['email']
  user = UserModel(email=email)
  db.session.add(user)
  db.session.commit()

  return "OK"

@app.get('/users')
def index():
  users = UserModel.query.all()
  return jsonify(users)

@app.get('/users/<string:id>')
def get(id):
  user = UserModel.query.filter_by(id=id).first()

  return jsonify(user)

@app.put('/users/<string:id>')
def update(id):
  user = UserModel.query.filter_by(id=id).first()

  newEmail = request.json['new_email']

  user.email = newEmail
  db.session.commit()

  return jsonify(user)

@app.delete('/users/<string:id>')
def delete(id):
  user = UserModel.query.filter_by(id=id).first()
  if(not user):
    print("NULL")
    return "NAO ENCONTRADO"

  db.session.delete(user)
  db.session.commit()

  return jsonify(user)
   

app.run(host='localhost', port=5000)