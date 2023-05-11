from flask.testing import FlaskClient
from src.models import db, User
from tests.utils import refresh_db


def test_login_page(test_client: FlaskClient):
    refresh_db()
    response = test_client.get("/login", follow_redirects=True)
    response_data = response.data.decode("utf-8")

    assert "<title>Login</title>" in response_data

    user = User(username="bob", password="1234")
    db.session.add(user)
    db.session.commit()

    response = test_client.post(
        "/login",
        query_string={"name": "user2", "password": "1234"},
        follow_redirects=True,
    )

    assert response.request.path == "/login"
