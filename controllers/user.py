from flask import jsonify
import bcrypt
from datetime import datetime
from db_config import db
from models.user import User
from models.good import Good
from schemas.user import user_schema


def create_user(username, firstname, lastname, birthdate, password):
    if (User.check_username_availability(username)):
        return {
            "error": "username exist"
        }
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    birhtdate_datetime = datetime.strptime(birthdate, '%d/%m/%Y')
    new_user = User(username, firstname, lastname,
                    birhtdate_datetime, hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)


def get_user(id):
    user = User.query.get(id)

    return user_schema.jsonify(user)


def update_user(id, username, firstname, lastname, birthdate, password):
  # if (User.check_username_availability(username)):
  #      return {
  #          "error": "username exist"
  #      }

    user = User.query.get(id)
    user.username = username
    user.firstname = firstname
    user.lastname = lastname
    user.birthdate = datetime.strptime(birthdate, '%d/%m/%Y')
    user.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    db.session.commit()

    return user_schema.jsonify(user)


def delete_user(id):
    user = User.query.get(id)
    goods = db.session.query(Good).filter(Good.user_id == id)
    db.session.delete(user)

    for good in goods:
      db.session.delete(good)

    db.session.commit()

    return user_schema.jsonify(user)
