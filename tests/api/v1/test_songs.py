from flask.testing import FlaskClient


def test_request_example(client: FlaskClient):
    response = client.get("/songs")
    assert {} in response.json
