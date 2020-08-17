from flask import request, jsonify
import os
from flask_jwt import JWT
from config import app
from db_config import db
from models.user import User
import routes.index

jwt = JWT(app, User.authenticate, User.identity)

if __name__ == '__main__':
    app.run(debug=True)
