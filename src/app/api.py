from src.app.config import *
from src.app.app import create_app

app = create_app()


@app.route("/")
def homepage():
    logger.info("Snowball GR homepage.")
    return app.send_static_file('homepage.html')