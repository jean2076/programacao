from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 
import os
import json

app = Flask(__name__)
CORS(app)  
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'aviao.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)