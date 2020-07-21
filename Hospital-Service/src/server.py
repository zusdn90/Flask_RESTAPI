import os
import sys, getopt
import schedule
import requests

from flask import Flask, request, Blueprint, jsonify
from flask_restplus import Api
from flask_restful import reqparse
from flaskext.mysql import MySQL
from flask_cors import CORS

from modules.control import user
from modules.control import database


from modules.rest.v01.ns_user import api as user_api, on_load as on_load_user
from modules.setting import dbConnector

# ============================ init Flask config ============================
app = Flask(__name__, static_folder='static', template_folder='template')

cors = CORS(app, resources={
  r"/api/*": {"origin": "*"},
})

blueprint = Blueprint('api', __name__, url_prefix='/api/v01')


api = Api(blueprint, doc='/doc/', version= 1.0, 
          title='HOSPITAL API', description='HOSPITAL REST API')

on_load_user(user)
api.add_namespace(user_api)

app.register_blueprint(blueprint)
app.config.SWAGGER_UI_DOC_EXPANSION = 'full'


db_class = dbConnector.Database()

@app.route('/', methods=['GET'])
def index():
    return "Index Page..."


@app.route('/users', methods=['GET'])
def select():    
    sql = "select * from Patient"
    data = db_class.executeAll(sql)

    return jsonify(data)

@app.route('/users', methods=['POST'])
def insert(object):
    try:
        sql = "insert into Patient \
               values('%s')" % ('testData') 
                              
        data = db_class.execute(sql)
        db_class.commit()

    except Exception as e:
        print(str(e))


def multiply(x, y):
    return x * y


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)