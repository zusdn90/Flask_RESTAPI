from flask import Flask, request, Blueprint, jsonify
from flask_restplus import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL
from flask_cors import CORS

from modules.control import user
from modules.control import database

from modules.rest.ns_user import api as user_api
from modules.setting import dbConnector


# ============================ init Flask config ============================

app = Flask(__name__, static_folder='static', template_folder='template')

cors = CORS(app, resources={
  r"/api/*": {"origin": "*"},
})

blueprint = Blueprint('api', __name__, url_prefix='/api')


api = Api(blueprint, doc='/doc/', version= 1.0, 
          title='HOSPITAL API', description='HOSPITAL REST API')

api.add_namespace(user_api)

app.register_blueprint(blueprint)

@app.route('/', methods=['GET'])
def index():
    return "Index Page..."


@app.route('/users', methods=['GET'])
def select():
    db_class = dbConnector.Database()
    sql = "select * from Patient"
    data = db_class.executeAll(sql)

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)