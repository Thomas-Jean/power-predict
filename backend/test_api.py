import pytest
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