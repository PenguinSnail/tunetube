from flask.testing import FlaskClient
from src.models import db, User
from tests.utils import refresh_db


def test_sign_up_page(test_client: FlaskClient):
    refresh_db()
    response = test_client.get("/account/register", follow_redirects=True)
    response_data = response.data.decode("utf-8")

    assert "<title>TuneTube - Account</title>" in response_data
    # Testing aadding a user that is already in the database
    user = User(username="bob", password="1234")
    db.session.add(user)
    db.session.commit()

    response = test_client.post(
        "/account/register",
        query_string={"name": "bob", "password": "1234", "confirm_password":"1234"},
        follow_redirects=True,
    )
  
    assert response.status_code == 500
    assert response.request.path == "/account/register"

    # Testing if the password do not match
    refresh_db()
    response = test_client.get("/account/register", follow_redirects=True)
    response_data = response.data.decode("utf-8")

    response = test_client.post(
        "/account/register",
        query_string={"name": "bob", "password": "1234", "confirm_password":"1"},
        follow_redirects=True,
    )
  
    assert response.status_code == 500
    assert response.request.path == "/account/register"

    # Testing that the user is created
    refresh_db()
    response = test_client.get("/account/register", follow_redirects=True)
    response_data = response.data.decode("utf-8")

    response = test_client.post(
        "/account/register",
        query_string={"name": "bob", "password": "1234", "confirm_password":"1234"},
        follow_redirects=True,
    )
  
    assert response.status_code == 200
    assert response.request.path == "/"