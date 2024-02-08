from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy() # database orm
ma = Marshmallow() # data serialization
bcrypt = Bcrypt() # password hashing
jwt = JWTManager() #json web token for authentication