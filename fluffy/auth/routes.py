from .. import db
from . import bp

from ..models.user import User
from flask import request


@bp.post('/register')
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')

    if username is None or password is None or email is None:
        return ({'message':'all fields are required', 'status':400},400)
    if User.query.filter_by(email=email).first() is not None :
        return ({'message':'The email already exists', 'status':409}, 409)
    else:
        u = User(email=email, name=username)
        u.set_password(password)
        db.session.add(u)
        db.session.commit()
    return ({'u':u}, 201)

@bp.post('/login')
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if email is not None and password is not None:
        user = User.query.filter_by(email=email).first()
    else:
        return ({'message':'The password and email are required', 'status': 400}, 400)
    
    
    if user is None or not user.check_password(password):
        return ({'message': 'The user or password are incorrect', 'status':401}, 401)
    else:
        return ({'data': {'name':user.name, 'email':user.email}, 'status':200}, 200)
        