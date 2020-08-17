from db_config import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.DateTime, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, firstname, lastname, birthdate, password):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.password = password
