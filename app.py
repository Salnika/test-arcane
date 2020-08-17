from flask import request, jsonify
import os
from config import app
from db_config import db
import routes.index

if __name__ == '__main__':
    app.run(debug=True)
