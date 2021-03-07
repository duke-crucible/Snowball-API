from flask import Flask
# from flask_cors import CORS
from src.app.config import *


def create_app(testing=False):
    app = Flask(__name__)

    app.secret_key = SESSION_KEY  # enables flask session
    app.testing = testing  # true for pytest-flask testing env

    # logger.info(f"Configuring app with: {config.__name__}.")

    # Enable CORS.
    # CORS(app)

    return app