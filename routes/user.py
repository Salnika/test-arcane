from flask import request, jsonify
from config import app
from models.user import User
from controllers.user import create_user as create_user_ctrl
from controllers.user import update_user as update_user_ctrl
from controllers.user import get_user as get_user_ctrl
from controllers.user import delete_user as delete_user_ctrl


@app.route('/user', methods=['POST'])
def add_user():
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    birthdate = request.json['birthdate']
    password = request.json['password']

    return create_user_ctrl(firstname, lastname, birthdate, password)


@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    birthdate = request.json['birthdate']
    password = request.json['password']

    return update_user_ctrl(id, firstname, lastname, birthdate, password)


@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    return get_user_ctrl(id)


@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    return delete_user_ctrl(id)
