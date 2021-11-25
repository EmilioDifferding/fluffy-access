from . import db
from werkzeug.security import generate_password_hash, check_password_hash


place_user = db.Table('place_user',db.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('place_id', db.Integer, db.ForeignKey('places.id'))
)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    places = db.relationship('Place', secondary=place_user, backref=db.backref('users', lazy='dynamic'), lazy='dynamic')    

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

        