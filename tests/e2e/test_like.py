from flask import Flask
from flask.testing import FlaskClient
from src.models import db, User, Post, LikedBy
from flask_bcrypt import Bcrypt
from src.repositories.user_repository import user_repository_singleton
from tests.utils import refresh_db, create_user, create_post

def test_likes(test_client: FlaskClient):
# SETUP
    refresh_db()

    with test_client.session_transaction() as session:
        test_user = create_user()

        session['user'] = {
            'user_id' : test_user.getID()
        }

    user1 = User('fake1', 'asjfioahuiosd')
    db.session.add(user1)
    db.session.commit()
    
    user2 = User('fake2', 'asjfioahuiosd')
    db.session.add(user2)
    db.session.commit()

    new_post = Post('fakePost', 
                    '[{"time":702,"frequency":261.63,"playing":true},{"time":795,"frequency":261.63,"playing":false},{"time":1018,"frequency":261.63,"playing":true},{"time":1137,"frequency":261.63,"playing":false}]',
                    user1.getID())
    db.session.add(new_post)
    db.session.commit()
    
    post1 = Post('fakePost', 
                    '[{"time":702,"frequency":261.63,"playing":true},{"time":795,"frequency":261.63,"playing":false},{"time":1018,"frequency":261.63,"playing":true},{"time":1137,"frequency":261.63,"playing":false}]',
                    user2.getID())
    db.session.add(post1)
    db.session.commit()     
    
    current_user = session['user']['user_id']
    
# test current user likes post1
    dataCount = LikedBy.query.count()
    assert dataCount == 0
    
    # confirms likes post
    response = test_client.post(f'/tunes/{post1.id}/like')
    assert response.status_code == 204
    
    # confirms there is a new like in the database
    dataCount = LikedBy.query.count()
    assert dataCount == 1
    
    # confirms that the like is passed into the database
    like = LikedBy.query.filter_by(post_id=post1.id, user_id=current_user).first()
    assert like.getPost_ID() == post1.id
    
    # confirms when current user unlikes post
    response = test_client.delete(f'/tunes/{post1.id}/like')
    assert response.status_code == 204
    
    # confirms there the like is off the database
    dataCount = LikedBy.query.count()
    assert dataCount == 0
    