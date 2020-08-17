from flask import request, jsonify
from config import app
from flask_jwt import jwt_required, current_identity
from models.user import User
from controllers.user import create_user as create_user_ctrl
from controllers.user import update_user as update_user_ctrl
from controllers.user import get_user as get_user_ctrl
from controllers.user import delete_user as delete_user_ctrl


@app.route('/user', methods=['POST'])
def add_user():
    username = request.json['username']
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    birthdate = request.json['birthdate']
    password = request.json['password']

    return create_user_ctrl(username, firstname, lastname, birthdate, password)


@app.route('/user', methods=['PUT'])
@jwt_required()
def update_user():
    username = request.json['username']
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    birthdate = request.json['birthdate']
    password = request.json['password']

    return update_user_ctrl(current_identity.id, username, firstname, lastname, birthdate, password)


@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    return get_user_ctrl(id)


@app.route('/user', methods=['DELETE'])
@jwt_required()
def delete_user():
    return delete_user_ctrl(current_identity.id)
