import os
import platform
import sys
import time
import traceback
import random
import schedule

from modules.setting import dbConnector

db_class = dbConnector.Database()

# 공통 Response object
class Result(object):
    returncode = 1
    stdout = ""
    stderr = ""

    def __init__(self, returncode, stdout, stderr):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr

class Package:

    def insert_random_data(self):
        try:
            
            _now_func = {
                '0' : 'now()', # PostgreSQL
                '1' : 'sysdate', # Oracle
                '2' : 'getdate()', # SQLServer2000
                '21' : 'getdate()', # SQLServer2005
                '23' : 'getdate()', # SQLServer2008
                '14' : 'NOW()', # MySQL
                '15' : 'NOW()', # MariaDB
                '11' : 'sysdate', # Tibero
                '31' : 'now()' # PostgreSQL
            }

            
            pre_number = random.sample(range(1,9), 6)
            post_number = random.sample(range(1,9), 7)

            pre_number = "".join([str(_) for _ in pre_number])
            post_number = "".join([str(_) for _ in post_number])

            registration_number = pre_number + "-" + post_number

            vital_number = random.randint(1, 200)

            # 환자 입원 데이터 생성
            sql = '''\
            INSERT INTO Patient (registration_number, patient_code, patient_name, vital_code, vital_value, admission_date) 
            VALUES ({registration_number}, '1', {pre_number}, 'v01', {vital_number}, {now_func});
            '''.format(now_func = _now_func['15'])

            #쿼리 실행
            result = db_class.execute(sql)
            db_class.commit()

        except Exception as e:
            return Result(1, "", str(e))


    # 5분마다 100개의 랜덤 데이터 생성(1. 환자 입원  2. 입원 환자의 바이탈 수치 변화)
    #schedule.every(5).minute.do(insert_random_data)