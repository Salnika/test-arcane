from app import db
import os
from models.good import Good
from models.user import User
from datetime import datetime
import bcrypt

if not os.path.exists('database'):
    os.makedirs('database')

if os.path.exists('database/db.sqlite'):
    os.remove('database/db.sqlite')

db.create_all()

good_seed = [
    {
        "user_id": 1,
        "name": "Maison de plage",
        "description": "Petite maison en bord de plage",
        "good_type": "house",
        "city": "Arcachon",
        "room_nb": 2,
        "owner_name": "Alexis Salnikoff"
    },
    {
        "user_id": 1,
        "name": "Grande Maison",
        "description": "Grande maison en bord de plage",
        "good_type": "house",
        "city": "Arcachon",
        "room_nb": 5,
        "owner_name": "Alexis Salnikoff"
    },
    {
        "user_id": 2,
        "name": "Grand Appartement",
        "description": "Appartement pres de la tour eiffel",
        "good_type": "flat",
        "city": "Paris",
        "room_nb": 3,
        "owner_name": "Martin Dupont"
    }
]

for good in good_seed:
    new_good = Good(good['user_id'], good['name'], good['description'],
                    good['good_type'], good['city'], good['room_nb'], good['owner_name'])
    db.session.add(new_good)


user_seed = [
    {
        "username": "alex",
        "firstname": "Alexis",
        "lastname": "Salnikoff",
        "birthdate": "11/02/1994",
        "password": "s3cr3t"
    },
    {
        "username": "mdupont",
        "firstname": "Martin",
        "lastname": "Dupont",
        "birthdate": "12/07/1978",
        "password": "dupont"
    }
]

for user in user_seed:
    new_user = User(user['username'], user['firstname'],
                    user['lastname'], datetime.strptime(user['birthdate'], '%d/%m/%Y'), bcrypt.hashpw(user['password'].encode('utf-8'), bcrypt.gensalt()))
    db.session.add(new_user)

db.session.commit()
