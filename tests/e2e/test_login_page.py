from flask.testing import FlaskClient
from src.models import db, User
from tests.utils import refresh_db


def test_login_page(test_client: FlaskClient):
    refresh_db()
    response = test_client.get("/login", follow_redirects=True)
    response_data = response.data.decode("utf-8")

    assert "<title>Login</title>" in response_data

    # Tesing incorrect password
    refresh_db()
    response = test_client.get("/login", follow_redirects=True)
    response_data = response.data.decode("utf-8")

    user = User(username="bob", password="1234")
    db.session.add(user)
    db.session.commit()

    response = test_client.post(
        "/login",
        data={"name": "bob", "password": "123"},
        follow_redirects=True,
    )

    assert response.status_code == 500
    assert response.request.path == "/login"

    # Testing incorrect username.
    refresh_db()
    response = test_client.get("/login", follow_redirects=True)
    response_data = response.data.decode("utf-8")
    
    user = User(username="bob", password="1234")
    db.session.add(user)
    db.session.commit()

    response = test_client.post(
        "/login",
        data={"name": "user2", "password": "1234"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert response.request.path == "/login"
    
    # Testing that the user is logged in
    refresh_db()
    response = test_client.get("/login", follow_redirects=True)
    response_data = response.data.decode("utf-8")

    test_client.post(
        "/account/register",
        data={"name": "bob", "password": "1234", "confirm_password":"1234"},
        follow_redirects=True,
    )

    response = test_client.post(
        "/login",
        data={"name": "bob", "password": "1234"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert response.request.path == "/"
