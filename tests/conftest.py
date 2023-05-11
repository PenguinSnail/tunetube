from app import app
import pytest

<<<<<<< Updated upstream
@pytest.fixture(scope='module')
def test_client():
    with app.app_context():
        yield app.test_client()
=======

@pytest.fixture(scope="module")
def test_app():
    with app.app_context():
        yield app.test_client()
>>>>>>> Stashed changes
