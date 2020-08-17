from db_config import db
import enum

class Good(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(350))
    good_type = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    room_nb = db.Column(db.Integer, nullable=False)
    owner_name = db.Column(db.String(100))

    def __init__(self, user_id, name, description, good_type, city, room_nb, owner_name):
        self.user_id = user_id
        self.name = name
        self.description = description
        self.good_type = good_type
        self.city = city
        self.room_nb = room_nb
        self.owner_name = owner_name
