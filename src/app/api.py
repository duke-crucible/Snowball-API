from src.app.config import *
from src.app.app import create_app
from src.app.db_app import *
from src.app.shib import *

app = create_app()
mongo_client, db, NetID, SeedsPool = db_connecttion()


@app.route("/")
def homepage():
    logger.info("Snowball GR homepage.")
    return app.send_static_file('homepage.html')