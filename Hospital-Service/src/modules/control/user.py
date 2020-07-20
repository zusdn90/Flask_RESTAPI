
import os
import platform
import sys
import time

from flask import jsonify
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



class Package(object):

    def __init__(self):
        self._rows = []


    def get(self, id):
        db_class = dbConnector.Database()
        sql = "select * from Patient"
        data = db_class.executeAll(sql)

        return jsonify(data) 