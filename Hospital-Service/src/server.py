import os
import sys, getopt
import schedule
import logging
import time
import requests

from flask import Flask, request, Blueprint, jsonify, make_response, render_template
from flask_restplus import Api, Resource
from flask_restful import reqparse
from flaskext.mysql import MySQL
from flask_cors import CORS

from modules.api.v01.ns_user import api as user_api
from modules.api.v01.ns_database import api as database_api
from modules.setting import dbConnector
from modules.setting import log as logger

# ============================ init Flask config ============================
app = Flask(__name__, static_folder='static', template_folder='template')

cors = CORS(app, resources={
  r"/api/*": {"origin": "*"},
})

blueprint = Blueprint('api', __name__, url_prefix='/api/v01')
api = Api(blueprint, doc='/doc/', version= 1.0, 
          title='HOSPITAL API', description='HOSPITAL REST API')

#공통 으로 사용되는 API
common = api.namespace('common', description='Common API')

api.add_namespace(user_api)
api.add_namespace(database_api)

app.register_blueprint(blueprint)

@app.route('/', methods=['GET'])
def index():
    return "Index Page..."

@app.route('/start', methods=['GET'])
def start_schedule():
    # 10초에 한번씩 실행 
    schedule.every(10).seconds.do(job)
    
    while True:
        schedule.run_pending()
    time.sleep(1)

def job():
    url = 'http://127.0.0.1:5002/api/v01/users'
    response = requests.get(url=url)
    logger.info_log("request get user list...")

class HttpStatusResponse(Resource):
    @app.errorhandler(404)
    def notFoundError(self):        
        return "[404] Page Not Found..."

    @app.errorhandler(400)
    def uncaughtError(self):
        return "[400] Bad request..."

    @app.errorhandler(401)
    def unauthorize(self):
        return "[401] Not unauthorized..."        

    @app.errorhandler(500)
    def serverError(self):
        return "[500] Server Error..."

if __name__ == '__main__':    
    app.run(host='127.0.0.1', port=5002, debug=True)