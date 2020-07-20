from flask import request
from flask_restplus import Namespace, Resource, fields, reqparse


api = Namespace('user', description = "User API")
parser = reqparse.RequestParser()


""" 
#################################################################
DATABASE API 
#################################################################
""" 

@api.route('/database')
class GetUserInfo(Resource):
    def get(self):
        pass

    def post(self):
        pass