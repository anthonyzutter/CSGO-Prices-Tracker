from . import db
from . import now
from flask_login import UserMixin
from sqlalchemy.sql import func
from steam_community_market import  AppID

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    items = db.relationship('Item')

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    current_price = db.Column(db.Float, default=0)
    url = db.Column(db.String(254), default="https://steamcommunity.com/market/listings/730/")
    date = db.Column(db.String(100), default=now.strftime("%d/%m/%Y"))
    game = db.Column(db.Integer(), default=AppID.CSGO)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
