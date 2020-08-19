import pytest
from datetime import datetime
from fastapi.testclient import TestClient
from fastapi import FastAPI

from . import api_v1

app = FastAPI()

app.include_router(api_v1.api_router, prefix="/api/v1")


@pytest.fixture
def client():
	client = TestClient(app)
	return client

def test_generic_response(client):
	
	response = client.get('/api/v1/power')
	response_body = response.json()


	assert response.status_code == 200
	assert isinstance(response_body, list)
	assert len(response_body) == 1

def test_single_date_response(client):
	
	response = client.get('/api/v1/power?start_date=2020-01-01')
	response_body = response.json()


	assert response.status_code == 200
	assert isinstance(response_body, list)
	assert len(response_body) == 1
	assert datetime.fromisoformat(response_body[0]['date']) == datetime(2020,1,1)


def test_date_range_response(client):
	
	response = client.get('/api/v1/power?start_date=2020-01-01&end_date=2020-01-31')
	response_body = response.json()


	assert response.status_code == 200
	assert isinstance(response_body, list)
	assert len(response_body) == 31

def test_unix_time_response(client):
	
	response = client.get('/api/v1/power?start_date=0')
	response_body = response.json()


	assert response.status_code == 200
	assert isinstance(response_body, list)
	assert len(response_body) == 1

def test_unprocessable_entity(client):
	
	response = client.get('/api/v1/power?start_date=x')
	response_body = response.json()


	assert response.status_code == 422
