import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate

from config import Config

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()


def create_app(test_config=None):
    # application factory function all config and registrations goes here
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    

    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    @app.route('/')
    def hello():
        return ({'config':app.config.get('SQLALCHEMY_DATABASE_URI')},200)
    
    from . import auth
    app.register_blueprint(auth.bp, url_prefix='/auth')
    # app.register_blueprint()
    return app

from . import models