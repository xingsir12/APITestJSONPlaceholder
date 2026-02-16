# conftest.py
import pytest
import requests
from utils.logger import logger

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def api_client():
    """Фикстура для API клиента"""
    logger.info("=" * 80)
    logger.info(" STARTING TEST SESSION")
    logger.info("=" * 80)
    
    from utils.api_client import APIClient
    client = APIClient(BASE_URL)
    
    yield client
    
    logger.info("=" * 80)
    logger.info(" TEST SESSION COMPLETED")
    logger.info("=" * 80)

@pytest.fixture
def sample_user():
    """Фикстура с тестовыми данными пользователя"""
    return {
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com"
    }

@pytest.fixture
def sample_post():
    """Фикстура с тестовыми данными поста"""
    return {
        "title": "Test Post",
        "body": "Test post content",
        "userId": 1
    }

# Хуки для логирования
def pytest_runtest_setup(item):
    logger.info(f"\n{'=' * 60}")
    logger.info(f" Running: {item.nodeid}")
    logger.info(f"{'=' * 60}")

def pytest_runtest_teardown(item, nextitem):
    logger.info(f" Finished: {item.name}\n")

def pytest_runtest_logreport(report):
    """Логирование результатов тестов"""
    if report.when == "call":
        if report.passed:
            logger.info(f"✅ PASSED: {report.nodeid}")
        elif report.failed:
            logger.error(f"FAILED: {report.nodeid}")
            logger.error(f"     Error: {report.longreprtext}")
        elif report.skipped:
            logger.warning(f"   SKIPPED: {report.nodeid}")