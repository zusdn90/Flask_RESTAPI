from flask import Flask, request, jsonify
from flask_restplus import Namespace, Resource, fields, reqparse

api = Namespace('users', description = "User API")
parser = reqparse.RequestParser()

user = None
Opts = None
db = None

def on_load(_user):
    global user

    user = _user


""" 
#################################################################
USER API (Patient)
#################################################################
""" 

@api.route('')
class GetUsersInfo(Resource):
    def get(self):
        try:
            pkg = user.Package
            res = pkg.get_user_list()

            return res

        except Exception as e:
            print(str(e))

    @api.param('body', '', 'body')
    def post(self):
        '''
        사용자가 보낸 session 정보를 통해
        수정 역할을 합니다.
        '''
        return {'msg': 'post ok'}

    def patch(self):
        '''
        사용자가 보낸 데이터를 저장한다.
        '''
        return {'msg': 'put ok'}

    def delete(self):
        '''
        데이터를 삭제한다.
        '''
        return {'msg': 'delete ok'}
