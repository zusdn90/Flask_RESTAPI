import json
import datetime
from flask import Flask, request, jsonify, make_response, request
from flask_restplus import Namespace, Resource, fields, reqparse
from modules.setting import dbConnector
from modules.setting import log as logger

parser = reqparse.RequestParser()
db_class = dbConnector.Database()

api = Namespace('users', description = "USER API")

""" 
#################################################################
USER API (Employee)
#################################################################
"""

class Result(object):
    returncode = 1
    stdout = ""
    stderr = ""

    def __init__(self, returncode, stdout, stderr):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


@api.route('')
class GetUsersInfo(Resource):    
    @api.param('Date', 'enter_date')
    def get(self):
        try:            
            parser.add_argument('Date', type=str, help='admisstion date')
            params = parser.parse_args()
            logger.info_log("params : " + str(params))

            sql = "select employee_name from Employee where employee_code = %s"
            convert_date = datetime.datetime.strptime(params['Date'], "%Y-%m-%d").date()
            rows = db_class.executeAll(sql, convert_date)

            logger.info_log("[User List Data] : " + str(rows))
            
            return {"status" : "200", "message": "Data select success..."}

        except Exception as e:            
            logger.error_log(str(e))           

    @api.param('employee_code', 'employee code')
    @api.param('employee_name', 'employee name')
    @api.param('address', 'address')
    @api.param('salary', 'salary')
    @api.param('phone_number', 'phone number')
    def post(self):
        try:
            parser.add_argument('employee_code', type=str, help='employee code')
            parser.add_argument('employee_name', type=str, help='employee name')
            parser.add_argument('address', type=str, help='address')
            parser.add_argument('salary', type=str, help='salary')
            parser.add_argument('phone_number', type=str, help='phone_number')     
            params = parser.parse_args()
            logger.info_log("params : " + str(params))

            data = request.get_json(silent=True, force=True)
            logger.info_log("Request data : " + str(data))

            sql = """\
            insert into Employee (employee_code, employee_name, address, salary, phone_number, date) 
                    values ( %s, %s, %s, %s, %s, now())
            """

            rows = db_class.execute(sql, (data["employee_code"], data["employee_name"], data["address"], data["salary"], data["phone_number"]))
            
            db_class.commit()
            db_class.close()

            logger.info_log("commit complete")
            
            return {"status" : "200", "message": "Data insert success..."}

        except Exception as e:
            logger.error_log(str(e))
        finally:
            db_class.close()
                        

    @api.param('employee_code','employee code')
    def patch(self):
        try:
            parser.add_argument('employee_code', type=str, help='Employee code')
            params = parser.parse_args()
            logger.info_log("params : " + str(params))

            data = request.get_json(silent=True, force=True)

            logger.info_log("Request data : " + str(data))

            sql = """\
            update Employee set 
                employee_name = %s,
                address = %s,
                salary = %s,
                phone_number = %s,                
                where employee_code = %s

            """            
            rows = db_class.execute(sql, (data["employee_name"], data["address"], data["salary"], data["phone_number"], data["employee_code"]))
            
            db_class.commit()
            db_class.close()

            logger.info_log("commit complete")
            
            return {"status" : "200", "message": "Data update success..."}

        except Exception as e:
            logger.error_log(str(e))
        finally:
            db_class.close()

    def delete(self):
        try:
            data = request.get_json(silent=True, force=True)

            logger.info_log("Request data : " + str(data))

            sql = """\
            delete from Employee where employee_code = %s
            """            
            rows = db_class.execute(sql, data["employee_code"])
            
            db_class.commit()
            db_class.close()

            logger.info_log("commit complete")
            
            return {"status" : "200", "message": "Data delete success..."}

        except Exception as e:
            logger.error_log(str(e))            
        finally:
            db_class.close()
