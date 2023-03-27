from flask.testing import FlaskClient

def test_home_page(test_app: FlaskClient):
    response = test_app.get('/')
    response_data = response.data.decode('utf-8')

    assert '<h1>TuneTube</h1>' in response_data
