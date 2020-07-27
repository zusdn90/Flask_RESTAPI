import unittest
import requests
import json

from modules.api.v01 import ns_user
from server import app

class UnitTest(unittest.TestCase):
    
    def setUp(self):
        self.host = 'http://127.0.0.1:5002'
        self.app = app.test_client()
        self.right_parameter = {
            'param1': 'test',
            'param2': 'dcvc',
            'param3': 2323
        }
        self.wrong_parameter = {
            'param1' : 'test'
        }

    def test_user_wrong_parameter(self):
        response = self.app.get(self.host+'/api/v01/users' ,data=self.wrong_parameter)
        data = json.loads(response.get_data())
        
        self.assertEqual('200', data['status'])
        self.assertEqual('Data select success...', data['mesaage'])


    def test_user_wrong_result(self):
        response = self.app.get(self.host + '/api/v01/users',data=self.wrong_parameter)
        data = json.loads(response.get_data())
        
        self.assertEqual('200', data['status'])
        self.assertEqual('Data select success...', data['mesaage'])        
        
if __name__ == '__main__':
    unittest.main()
    