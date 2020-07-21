from flask import Flask, request, jsonify
from flask_restplus import Namespace, Resource, fields, reqparse
from modules.setting import dbConnector

parser = reqparse.RequestParser()
db_class = dbConnector.Database()

api = Namespace('users', description = "USER API")

""" 
#################################################################
USER API (Patient)
#################################################################
""" 


class Result(object):
    returncode = 1
    status = ""
    stdout = ""
    stderr = ""

    def __init__(self, returncode, status, stdout, stderr):
        self.returncode = returncode
        self.status = status
        self.stdout = stdout
        self.stderr = stderr



@api.route('')
class GetUsersInfo(Resource):
    def get(self):
        try:
            sql = "select * from patient"
            data = db_class.executeAll(sql)

            return Result(0, "200", jsonify(data), "")
        except Exception as e:            
            return Result(1, "500","", str(e))

    def post(self):
        try:
            sql = "insert into Patient \
                    values(%s, %s, %s, %s, %s, %s)" % ('','','','','','') 
                              
            data = db_class.execute(sql)
            db_class.commit()

        except Exception as e:
            print(str(e))

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
