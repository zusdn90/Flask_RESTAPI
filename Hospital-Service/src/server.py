from flask import Flask, request, Blueprint
from flask_restplus import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={
  r"/api/*": {"origin": "*"},
})

blueprint = Blueprint('api', __name__, url_prefix='/api')


api = Api(blueprint, version= 1.0, 
          title='HOSPITAL API', description='HOSPITAL REST API')

# DB(Mysql) 연결
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'matrix_hhw'
app.config['MYSQL_DATABASE_PASSWORD'] = 'matrix_hhw'
app.config['MYSQL_DATABASE_DB'] = 'matrix_hhw'
app.config['MYSQL_DATABASE_HOST'] = '192.168.0.50'
mysql.init_app(app)


app.register_blueprint(blueprint)




class CreatUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('patient_code', type=int)
            parser.add_argument('patient_name', type=str)
            parser.add_argument('patient_age', type=str)
            parser.add_argument('alert_info', type=str)
            args = parser.parse_args()

            _userCode = args['patient_code']
            _userName = args['patient_name']
            _userAge = args['patient_age']
            _alertInfo = args['alert_info']

            
            #return {'Email': args['email'], 'UserName': args['user_name'], 'Password': args['password']}

        except Exception as e:
            return {'error': str(e)}


api.add_resource(CreatUser, '/user')

if __name__ == '__main__':
    app.run(debug=True)