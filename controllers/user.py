from flask import jsonify
import bcrypt
from datetime import datetime
from db_config import db
from models.user import User
from schemas.user import user_schema


def create_user(firstname, lastname, birthdate, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    birhtdate_datetime = datetime.strptime(birthdate, '%d/%m/%Y')
    new_user = User(firstname, lastname, birhtdate_datetime, hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)


def get_user(id):
    user = User.query.get(id)

    return user_schema.jsonify(user)


def update_user(id, firstname, lastname, birthdate, password):
    user = User.query.get(id)
    user.firstname = firstname
    user.lastname = lastname
    user.birthdate = birthdate
    user.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    db.session.commit()

    return user_schema.jsonify(user)


def delete_user(id):
    user = User.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)
