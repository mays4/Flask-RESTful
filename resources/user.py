from flask_restful import Resource,reqparse

import sqlite3
from models.user import UserModel

class UserRgister(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('username',type=str,required=True,help="This field cannot be blank") 
  parser.add_argument('password',type=str,required=True,help="This field cannot be blank")
  def post(self):
    data = UserRgister.parser.parse_args()

    if UserModel.find_by_username(data['username']):
      return{"message":"User with this username already exist"},400
    user = UserModel(**data)
    user.save_to_db()

    return {"message":"User created successfully."},201