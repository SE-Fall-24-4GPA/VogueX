# VogueX
# Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
# DB_NAME = "database.db"
# db_overlay = None


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "akjdnauhdbas asdnabdbaskd"
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mysql+pymysql://admin:0311@localhost:3306/fashion"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    if test_config:
        app.config["SECRET_KEY"] = test_config["SECRET_KEY"]
        app.config["SQLALCHEMY_DATABASE_URI"] = test_config["SQLALCHEMY_DATABASE_URI"]

    db.init_app(app)

    from .views import views
    from .auth import auth
    from .favourites import favouritesbp

    from . import preferences
    from . import recommendations
    from . import shopping

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(favouritesbp, url_prefix="/")
    app.register_blueprint(preferences.preferencesbp)
    app.register_blueprint(recommendations.recommendationsbp)
    app.register_blueprint(shopping.shoppingbp)

    from .models import User

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
