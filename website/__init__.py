from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'fhuewf frbeuwobfr'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # from . import models
    from .models import User, Note  # The reason y we are importing is to load the db schema
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # redirect user to login page if not logged in
    login_manager.init_app(app)


    # function to load fetch the user and load
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


''' Flask-SQLAlchemy 3 no longer accepts an app argument to methods like create_all '''
# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')
