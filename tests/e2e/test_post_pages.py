from flask import Flask
from flask.testing import FlaskClient
from src.models import db, User, Post
from flask_bcrypt import Bcrypt
from src.repositories.user_repository import user_repository_singleton
from tests.utils import refresh_db, create_user, create_post
from app import session

def test_post_pages(test_client: FlaskClient):
    refresh_db()

    with test_client.session_transaction() as session:
        test_user = create_user()

        session['user'] = {
            'user_id' : test_user.getID
        }

    test_post = create_post(post=session['user_id'])

    # Now you should be able to go into the test files. 

    # response = test_client.post('/account/register', query_string={
    #     'name': 'user', 'password': '1234', 'confirm_password': '1234' 
    # }, follow_redirects=True)


    # test_client.post('/tunes', query_string={
    #     'title':'My Song', 
    #     'data':'[{"time":702,"frequency":261.63,"playing":true},{"time":795,"frequency":261.63,"playing":false},{"time":1018,"frequency":261.63,"playing":true},{"time":1137,"frequency":261.63,"playing":false}]'
    #     }, follow_redirects=True, cookies={'session': session})
    


    # response = test_client.get('/tunes', cookies={'session': session})
    # response_data = response.data.decode('utf-8')
    # assert 'My Song' in response_data

