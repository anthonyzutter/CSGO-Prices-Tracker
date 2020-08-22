from flask import Flask, jsonify 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json 
import os

app = Flask(__name__)

path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'item.db')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
