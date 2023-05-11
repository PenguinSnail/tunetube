# from flask import Flask
# from flask.testing import FlaskClient
# from src.models import db, User
# from flask_bcrypt import Bcrypt
# from src.repositories.user_repository import user_repository_singleton
# from tests.utils import refresh_db

# def test_login_page(test_app: FlaskClient):
#     # refresh_db()
#     response = test_app.get("/login", follow_redirects=True)
#     response_data = response.data.decode("utf-8")

#     assert "<title>Login</title>" in response_data

#     user = User(username='bob', password='1234')
#     db.session.add(user)
#     db.session.commit()

#     response = test_app.post('/login', query_string={
#         'name': 'user2', 'password': '1234' 
#     }, follow_redirects=True)

#     assert response.request.path == "/"



