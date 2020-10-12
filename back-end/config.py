from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

import json 
import os

app = Flask(__name__)
CORS(app)

now = datetime.now()

path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'item.db')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
