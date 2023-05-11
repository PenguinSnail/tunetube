from flask.testing import FlaskClient

def test_landing_page(test_client: FlaskClient):
    response = test_client.get("/", follow_redirects=True)
    response_data = response.data.decode("utf-8")

    assert "<title>TuneTube</title>" in response_data
    assert "Get Started</button>" in response_data
    assert "Login</button>" in response_data
