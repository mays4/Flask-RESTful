from models.user import UserModel
# from werkzeug.security import safe_str_cmp 
# users=[ User(1,'bob','asdf')]

# username_mapping ={ u.username:u for u in users

# }
# userid_mapping = { u.id :u for u in users

# }


def authenticate(username,password):
  user = UserModel.find_by_username(username)
  #user = username_mapping.get(username,None)
    # if user and safe_str_cmp(user.password, password):
  if user and user.password == password:
    return user

def identity(payload):
  user_id = payload['identity']
  # return userid_mapping.get(user_id,None)
  return UserModel.find_by_id(user_id)
     