# from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import JWTManager
# from flask_migrate import Migrate
# from flask_cors import CORS

# db = SQLAlchemy()
# jwt = JWTManager()
# migrate = Migrate()
# cors = CORS()

# app/extensions.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db      = SQLAlchemy()
migrate = Migrate()
jwt     = JWTManager()
cors    = CORS()
