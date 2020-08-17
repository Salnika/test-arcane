from flask import request, jsonify
from config import app
from flask_jwt import jwt_required, current_identity
from controllers.good import create_good as create_good_ctrl
from controllers.good import get_all_user_goods as get_all_user_goods_ctrl
from controllers.good import update_good as update_good_ctrl
from controllers.good import delete_good as delete_good_ctrl
from controllers.good import search_good as search_good_ctrl


@app.route('/good', methods=['POST'])
@jwt_required()
def create_good():
    name = request.json['name']
    description = request.json['description']
    good_type = request.json['good_type']
    city = request.json['city']
    room_nb = request.json['room_nb']
    owner_name = request.json['owner_name']
    return create_good_ctrl(current_identity.id, name, description, good_type, city, room_nb, owner_name)


@app.route('/good', methods=['GET'])
@jwt_required()
def get_all_user_goods():
    return get_all_user_goods_ctrl(current_identity.id)


@app.route('/good/<id>', methods=['PUT'])
@jwt_required()
def update_good(id):
    name = request.json['name']
    description = request.json['description']
    good_type = request.json['good_type']
    city = request.json['city']
    room_nb = request.json['room_nb']
    owner_name = request.json['owner_name']
    return update_good_ctrl(current_identity.id, id, name, description, good_type, city, room_nb, owner_name)


@app.route('/good/<id>', methods=['DELETE'])
@jwt_required()
def delete_good(id):
    return delete_good_ctrl(current_identity.id, id)


@app.route('/good/search/<city>', methods=['GET'])
def search_good(city):
    return search_good_ctrl(city)
