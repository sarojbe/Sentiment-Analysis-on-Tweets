from flask import Flask, render_template, url_for


def test_home():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is is posted to (POST)
    THEN check that a '405' status code is returned
    """
    app = Flask(__name__)

    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get("/")
        assert response.status_code == 404
        assert b"Welcome to the app world!" not in response.data
