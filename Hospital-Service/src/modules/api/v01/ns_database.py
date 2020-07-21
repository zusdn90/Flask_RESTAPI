import pymysql
import schedule
import openpyxl
import random
import string
from openpyxl import Workbook, load_workbook
from faker import Faker
from flask import request
from flask_restplus import Namespace, Resource, fields, reqparse
from modules.setting import dbConnector

parser = reqparse.RequestParser()
api = Namespace('database', description = "DATABASE API")

path = 'C:/Users/HONG/Desktop/Project/Aitrics/Hospital-Service/src/modules/data/'

""" 
#################################################################
DATABASE API 
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


@api.route('/create')
class CreateData(Resource):
    def get(self):
        return {'msg': 'get ok'}

    def post(self):
        faker = Faker()

        write_wb = Workbook()
    
        write_ws = write_wb.active
        write_ws['A1'] = 'patient_code'
        write_ws['B1'] = 'patient_name'
        write_ws['C1'] = 'vital_code'
        write_ws['D1'] = 'vital_value'
        write_ws['E1'] = 'alert_info'
        write_ws['F1'] = 'admission_date'

        for i in range(100):
            write_ws.append([str(i+1), faker.name(),'v01',faker.random_int(),'',faker.date_this_year()])
        
        write_wb.save(path + 'user_data.xlsx')

        return {"status" : "200", "message": "Data create success..."}

@api.route('/insert')
class InsertData(Resource):
    def get(self):
        return {'msg': 'get ok'}

    def post(self):
        db_class = dbConnector.Database()

        try:
            sql = 'insert into Patient values(%s, %s, %s, %s, %s, %s)'
    
            wb = load_workbook(path + '/user_data.xlsx', data_only=True)
            ws = wb['Sheet']
    
            iter_rows = iter(ws.rows)
                
            next(iter_rows)
                
            for row in iter_rows:
                db_class.execute(sql, (row[0].value, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value))
            db_class.commit()
        except Exception as e:            
            return Result(1, "500", str(e))
        finally:
            db_class.close()
            wb.close()


        

