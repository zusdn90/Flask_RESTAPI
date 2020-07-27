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
USER API (Patient)
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

            sql = "select patient_name from Patient where patient_code = %s"
            convert_date = datetime.datetime.strptime(params['Date'], "%Y-%m-%d").date()
            rows = db_class.executeAll(sql, convert_date)

            logger.info_log("[User List Data] : " + str(rows))
            
            return {"status" : "200", "message": "Data select success..."}

        except Exception as e:            
            logger.error_log(str(e))           

    @api.param('patient_code', 'patient code')
    @api.param('patient_name', 'patient name')
    @api.param('vital_code', 'vital code')
    @api.param('vital_value', 'vital value')
    @api.param('alert_info', 'alert info')
    def post(self):
        try:
            parser.add_argument('patient_code', type=str, help='Patient code')
            parser.add_argument('patient_name', type=str, help='Patient name')
            parser.add_argument('vital_code', type=str, help='Vital code')
            parser.add_argument('vital_value', type=str, help='Vital name')
            parser.add_argument('alert_info', type=str, help='Alert info')            
            params = parser.parse_args()
            logger.info_log("params : " + str(params))

            data = request.get_json(silent=True, force=True)
            logger.info_log("Request data : " + str(data))

            sql = """\
            insert into Patient (patient_code, patient_name, vital_code, vital_value, alert_info, date) 
                    values ( %s, %s, %s, %s, %s, now())
            """

            rows = db_class.execute(sql, (data["user_code"], data["user_name"], data["vital_code"], data["vital_value"], data["alert_info"]))
            
            db_class.commit()
            db_class.close()

            logger.info_log("commit complete")
            
            return {"status" : "200", "message": "Data insert success..."}

        except Exception as e:
            logger.error_log(str(e))
        finally:
            db_class.close()
                        

    @api.param('patient_code','paient code')
    def patch(self):
        try:
            parser.add_argument('patient_code', type=str, help='Patient code')
            params = parser.parse_args()
            logger.info_log("params : " + str(params))

            data = request.get_json(silent=True, force=True)

            logger.info_log("Request data : " + str(data))

            sql = """\
            update Patient set 
                patient_name = %s,
                vital_code = %s,
                vital_value = %s,
                alert_info = %s
                where patient_code = %s

            """            
            rows = db_class.execute(sql, (data["user_name"], data["vital_code"], data["vital_value"], data["alert_info"], data["user_code"]))
            
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
            delete from Patient where patient_code = %s
            """            
            rows = db_class.execute(sql, data["user_code"])
            
            db_class.commit()
            db_class.close()

            logger.info_log("commit complete")
            
            return {"status" : "200", "message": "Data delete success..."}

        except Exception as e:
            logger.error_log(str(e))            
        finally:
            db_class.close()
