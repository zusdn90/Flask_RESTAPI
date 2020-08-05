import unittest
import pytest
import json

from modules.api.v01 import ns_database
from server import app

@pytest.fixture
def client():
    client = app.test_client()

    yield client

def test_data_create_ok(client):
    rv = client.get('/api/v01/datas/create' ,data=dict(), follow_redirects=True)
    assert '200' in json.loads(rv.data.decode("utf-8"))['status']


def test_data_create_error(client):
    rv = client.post('/api/v01/datas/create',data=dict(), follow_redirects=True)
    assert '200' in json.loads(rv.data.decode("utf-8"))['status']



def test_data_insert_ok(client):
    rv = client.get('/api/v01/datas/insert' ,data=dict(), follow_redirects=True)
    assert '200' in json.loads(rv.data.decode("utf-8"))['status']


def test_data_insert_error(client):
    rv = client.post('/api/v01/datas/insert',data=dict(), follow_redirects=True)
    assert '200' in json.loads(rv.data.decode("utf-8"))['status']

        
if __name__ == '__main__':
    unittest.main()