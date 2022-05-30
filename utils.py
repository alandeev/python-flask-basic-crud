from flask import jsonify

def httpResponse(obj, statusCode = 200):
  return jsonify(obj), statusCode