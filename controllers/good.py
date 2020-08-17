from flask import jsonify
from sqlalchemy import func
from db_config import db
from models.good import Good
from schemas.good import good_schema, goods_schema
from error_handler import Error


def create_good(user_id, name, description, good_type, city, room_nb, owner_name):
    new_good = Good(user_id, name, description,
                    good_type, city, room_nb, owner_name)

    db.session.add(new_good)
    db.session.commit()

    return good_schema.jsonify(new_good)


def get_all_user_goods(user_id):
    goods = db.session.query(Good).filter(Good.user_id == user_id)
    return goods_schema.jsonify(goods)


def update_good(current_user_id, id, name, description, good_type, city, room_nb, owner_name):
    good = Good.query.get(id)
    if (good.user_id != current_user_id):
        raise Error('Invalid good ID', 403)

    good.name = name
    good.description = description
    good.good_type = good_type
    good.city = city
    good.room_nb = room_nb
    good.owner_name = owner_name

    db.session.commit()
    return good_schema.jsonify(good)


def delete_good(current_user_id, id):
    good = Good.query.get(id)
    if (good.user_id != current_user_id):
        raise Error('Invalid good ID', 403)

    db.session.delete(good)
    db.session.commit()
    return get_all_user_goods(current_user_id)


def search_good(city):
    goods = db.session.query(Good).filter(
        func.lower(Good.city) == func.lower(city))
    return goods_schema.jsonify(goods)
