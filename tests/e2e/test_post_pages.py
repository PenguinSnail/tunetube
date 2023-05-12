from flask import Flask
from flask.testing import FlaskClient
from src.models import db, User, Post
from flask_bcrypt import Bcrypt
from src.repositories.user_repository import user_repository_singleton
from tests.utils import refresh_db, create_user, create_post

def test_post_pages(test_client: FlaskClient):
    refresh_db()

    with test_client.session_transaction() as session:
        test_user = create_user()

        session['user'] = {
            'user_id' : test_user.getID()
        }

    
    new_user = User('fake', 'asjfioahuiosd')
    db.session.add(new_user)
    db.session.commit()

    new_post = Post('fakePost', '[{"time":702,"frequency":261.63,"playing":true},{"time":795,"frequency":261.63,"playing":false},{"time":1018,"frequency":261.63,"playing":true},{"time":1137,"frequency":261.63,"playing":false}]', new_user.getID())
    db.session.add(new_post)
    db.session.commit()

    # Now you should be able to go into the test files. 

    response = test_client.post('/tunes', data={ # ensure an actual post request works
        'title':'My Song', 
        'data':'[{"time":702,"frequency":261.63,"playing":true},{"time":795,"frequency":261.63,"playing":false},{"time":1018,"frequency":261.63,"playing":true},{"time":1137,"frequency":261.63,"playing":false}]'
        }, follow_redirects=True)

    assert response.status_code == 200

    response = test_client.get('/')
    response_data = response.data.decode('utf-8')

    assert 'My Song' in response_data
    assert 'fakePost' in response_data

    response = test_client.get('/tunes')
    response_data = response.data.decode('utf-8')

    assert 'My Song' in response_data
    assert 'fakePost' not in response_data

    # I had to do this using the current session's ID to make sure that the actual delete request via URL worked with the session
    newer_post = Post('deleteme', '[{"time":702,"frequency":261.63,"playing":true},{"time":795,"frequency":261.63,"playing":false},{"time":1018,"frequency":261.63,"playing":true},{"time":1137,"frequency":261.63,"playing":false}]', session['user']['user_id'])
    db.session.add(new_post)
    db.session.commit()

    test_client.delete(f'/tunes/{newer_post.getID()}')

    response = test_client.get('/')
    response_data = response.data.decode('utf-8')

    assert 'deleteme' not in response_data



