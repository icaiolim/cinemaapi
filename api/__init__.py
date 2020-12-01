# -*-coding: utf-8 -*-
from flask import Blueprint, Flask
from flask_cors import CORS
from flask_restx import Api
from flask_restx.apidoc import apidoc
from .config import *

# Define API Endpoint
URL_PREFIX = '/api'
apidoc.url_prefix = URL_PREFIX

# Database Instance with SQLAlchemy

# Marshmallow Instance

# Flask Instance
app = Flask(__name__)

# CORS Instance
cors = CORS(app)
CORS(app, resources=r'/api/*')

# Blueprint instance: modularization API
blueprint = Blueprint('/api', __name__, url_prefix=URL_PREFIX)

# Instance Flask-RestX
api = Api(
    version = '1.0',
    title = 'Cinema API',
    description = 'Serviço para consulta de filmes'
)

configure_app(app)
configure_restx(app)
configure_log()

