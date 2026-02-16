import pytest
import requests

from utils.api_client import APIClient

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
# Фикстура для API клиента
def api_client():
    return APIClient(BASE_URL)

@pytest.fixture
def sample_user():
    return {
        "name" : "Test User",
        "username" : "testuser",
        "email": "test@example.com"
    }

@pytest.fixture
def sample_post():
    return {
        "title": "Test Post",
        "body" : "Test post content",
        "userId": 1
    }

def pytest_runtest_setup(item):
    print(f"\nRunning: {item.name}")

def pytest_runtest_teardown(item, nextitem):
    print(f"Finished: {item.name}")