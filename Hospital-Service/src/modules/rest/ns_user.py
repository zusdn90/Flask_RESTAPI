from flask import request
from flask_restplus import Namespace, Resource, fields, reqparse


api = Namespace('user', description = "User API")
parser = reqparse.RequestParser()


""" 
#################################################################
USER API (Patient)
#################################################################
""" 

@api.route('/users')
class GetUserInfo(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
