import unittest
import pytest
import json

from modules.api.v01 import ns_user
from server import app

@pytest.fixture
def client():
    client = app.test_client()
    
    yield client

def test_user_select_ok(client):
    rv = client.get('/api/v01/users' ,data=dict(), follow_redirects=True)
    assert '200' in json.loads(rv.data.decode("utf-8"))['status']


def test_user_select__error(client):
    rv = client.post('/api/v01/users',data=dict(), follow_redirects=True)
    assert '200' in json.loads(rv.data.decode("utf-8"))['status']

        
if __name__ == '__main__':
    unittest.main()
    