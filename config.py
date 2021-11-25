import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
        SECRET_KEY = os.environ.get('SECRET_KEY')
        ENV=os.environ.get('FLASK_ENV')
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                'sqlite:///' + os.path.join(basedir, 'app.db')