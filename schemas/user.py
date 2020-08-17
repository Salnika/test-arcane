from ma_config import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'firstname', 'lastname', 'birthdate')


user_schema = UserSchema()
