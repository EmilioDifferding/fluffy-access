# from sqlalchemy.orm import backref
from . import db

class Place(db.Model):
    __tablename__ = 'places'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    keyname = db.Column(db.String(64), index=True)
    users = db.relationship('User', backref='place', lazy=True)