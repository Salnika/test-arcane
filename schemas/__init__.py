from ma_config import ma

class UserSchema(ma.Schema):
  class Meta:
    fileds = ('id', 'firstname', 'lastname', 'birthdate')

user_schema = UserSchema()