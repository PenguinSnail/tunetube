from app import app
import pytest

@pytest.fixture(scope='module')
def test_client():
    with app.app_context():
        yield app.test_client()