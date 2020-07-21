import os
import sys, getopt
import schedule
import requests

from flask import Flask, request, Blueprint, jsonify
from flask_restplus import Api
from flask_restful import reqparse
from flaskext.mysql import MySQL
from flask_cors import CORS

from modules.api.v01.ns_user import api as user_api
from modules.api.v01.ns_database import api as database_api
from modules.setting import dbConnector

# ============================ init Flask config ============================
app = Flask(__name__, static_folder='static', template_folder='template')

cors = CORS(app, resources={
  r"/api/*": {"origin": "*"},
})

blueprint = Blueprint('api', __name__, url_prefix='/api/v01')
api = Api(blueprint, doc='/doc/', version= 1.0, 
          title='HOSPITAL API', description='HOSPITAL REST API')

api.add_namespace(user_api)
api.add_namespace(database_api)

app.register_blueprint(blueprint)

@app.route('/', methods=['GET'])
def index():
    return "Root Page..."

def multiply(x, y):
    return x * y

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)