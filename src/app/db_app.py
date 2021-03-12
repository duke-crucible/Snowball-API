from src.app.config import *
from flask import Flask
from pymongo import MongoClient, errors
import sys


def db_connecttion():
    mongo_client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=MAX_SERVER_SEL_DELAY)
    logger.info("database URL:" + MONGO_URI)
    logger.info("db name:" + MONGODB_NAME)
    db = mongo_client[MONGODB_NAME]

    # check database connection status
    db_connection_status(mongo_client)

    try:
        NetID = db["NetID"]
        SeedsPool = db["SeedsPool"]
    except AttributeError as err:
        logger.error(str(err))
        sys.exit("Cannot connect to database collections. Exit.")

    return mongo_client, db, NetID, SeedsPool


def db_connection_status(mongo_client):
    logger.info("checking database connection...")
    try:
        logger.info(mongo_client.server_info())
        # server info example:
        # {'version': '3.6.0', 'versionArray': [3, 6, 0, 0], 'bits': 64, 'maxBsonObjectSize': 16777216, 'ok': 1.0}
        logger.info("database connection is successful.")
    except errors.ServerSelectionTimeoutError as err:
        logger.error(err)
        sys.exit("Database connection failed! Exit.")
