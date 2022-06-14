from flask import Flask, jsonify, request
from chat_bot import ask_bot
from models import db, UserModel, TaskModel
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS

from utils import httpResponse

app = Flask(__name__)
CORS(app)

app.config["JWT_EXPIRE_DAYS"] = 7
app.config["SECRET_KEY"] = "123456"

jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
  db.create_all()

# rota de testes <
@app.get("/users")
def getAllUsers():
  users = UserModel.query.all()    
  return httpResponse(users)

@app.post("/auth/login")
def authLogin():
  username = request.json['username']
  user = UserModel.query.filter_by(username=username).first()
  if(not user):   
    responseError = { "message": "Username not found"}
    
    return httpResponse(responseError, 401)
    
  jwtToken = create_access_token(identity=user.id)
    
  return httpResponse({ "token": jwtToken })


@app.post("/auth/register")
def authRegister():
  try:
    username = request.json['username']
    user = UserModel.query.filter_by(username=username).first()
    if(user):
      responseError = { "message": "username already exist"}
    
      return httpResponse(responseError, 400)

    user = UserModel(username=username)
    db.session.add(user)
    db.session.commit()

    return httpResponse(user, 201)
  except Exception as e:
    print(e)
    responseObject = { "message": "internal server error" }

    return httpResponse(responseObject, 500)

@app.get('/tasks')
@jwt_required()
def listTasks():
  userId = get_jwt_identity()
  tasks = TaskModel.query.filter_by(user_id=userId).all()

  return httpResponse(tasks)

@app.post('/tasks')
@jwt_required()
def createTask():
  userId = get_jwt_identity()
  user = UserModel.query.filter_by(id=userId).first()
  if(not user):
    responseError = { "message": "User does not exist" }
    return httpResponse(responseError, 401)

  task = TaskModel(
    user_id = userId,
    title = request.json['title'],
    description = request.json['description'],
    status = request.json['status']
  )

  db.session.add(task)
  db.session.commit()

  return httpResponse(task, 201)

@app.get('/tasks/<string:id>')
@jwt_required()
def getTask(id):
  task = TaskModel.query.filter_by(id=id).first()
  if(not task):
    responseError = { "message": "Task not found" }
    return httpResponse(responseError, 404)

  userId = get_jwt_identity()

  if(task.user_id != userId):
    responseError = { "message": "Task not found" }
    return httpResponse(responseError, 403)

  return httpResponse(task)

@app.put('/tasks/<string:id>')
@jwt_required()
def updateTask(id):
  task = TaskModel.query.filter_by(id=id).first()
  if(not task):
    responseError = { "message": "Task not found" }
    return httpResponse(responseError, 404)

  userId = get_jwt_identity()

  if(task.user_id != userId):
    responseError = { "message": "Task not found" }
    return httpResponse(responseError, 403)

  task.title = request.json['title']
  task.description = request.json['description']
  task.status = request.json['status']
  db.session.commit()

  return httpResponse(task)

@app.delete('/tasks/<string:id>')
@jwt_required()
def deleteTask(id):
  task = TaskModel.query.filter_by(id=id).first()
  if(not task):
    responseError = { "message": "Task not found" }
    return httpResponse(responseError, 404)

  userId = get_jwt_identity()

  if(task.user_id != userId):
    responseError = { "message": "Task not found" }
    return httpResponse(responseError, 403)


  db.session.delete(task)
  db.session.commit()

  return httpResponse({}, 204)

@app.get('/profile')
@jwt_required()
def userProfile():
  userId = get_jwt_identity()

  user = UserModel.query.filter_by(id=userId).first()
  tasks = TaskModel.query.filter_by(user_id=userId).all()

  responseObject = {
    "username": user.username,
    "tasks": tasks
  }

  return httpResponse(responseObject, 200)

@app.put('/users')
@jwt_required()
def update():
  userId = get_jwt_identity()
  user = UserModel.query.filter_by(id=userId).first()

  user.username = request.json['username']
  db.session.commit()

  return httpResponse(user, 200)

@app.delete('/users')
@jwt_required()
def delete():
  userId = get_jwt_identity()
  user = UserModel.query.filter_by(id=userId).first()

  db.session.delete(user)
  db.session.commit()

  return httpResponse({}, 204)

@app.post('/chat_bot')
def chat_bot():
  content = request.json['content']
  answer = ask_bot(content)

  responseObject = {
    "awsrer": answer
  }

  return httpResponse(responseObject, 200) 
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)