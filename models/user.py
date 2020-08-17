from db_config import db
import bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.DateTime, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, firstname, lastname, birthdate, password):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.password = password

    @staticmethod
    def authenticate(username, password):
        user = db.session.query(User).filter(User.username == username).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
            return user

    @staticmethod
    def identity(payload):
        user_id = payload['identity']
        user = db.session.query(User).filter(User.id == user_id).first()
        return user
