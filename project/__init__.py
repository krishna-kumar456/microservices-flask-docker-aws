from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
import os

#instantiate the extensions
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app():

    # instantiate the app
    app = Flask(__name__)
   
    CORS(app)
    
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)


    # setup extentensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # register blueprints
    from project.api.users  import users_blueprint
    app.register_blueprint(users_blueprint)
    from project.api.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)

    print(app)
    
    return app

    
