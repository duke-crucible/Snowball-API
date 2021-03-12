import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from src.app.config import logger,SENDGRID_FROM_ADDRESS,TTLD_GENERATION_TO_CONSENT,SENDGRID_API_KEY
from xkcdpass import xkcd_password as xp
from flask import make_response
import json
import os, sys
import csv
import pandas as pd
from pymongo import MongoClient
from datetime import date

# send email via sendgrid template
def send_email(recipient, token, template_id):
    # Build the invitation email and submit the request to SendGrid
    logger.info("Sending email through sendgrid to recipient:" + recipient)
    # if send plaintext only:
    # content = Content("text/plain", "")
    # https://github.com/sendgrid/sendgrid-python
    message = Mail(
        from_email = SENDGRID_FROM_ADDRESS,
        to_emails = recipient,
    )
    expire_date = datetime.datetime.today() + datetime.timedelta(days=int(TTLD_GENERATION_TO_CONSENT))
    date_time = expire_date.strftime("%m-%d-%Y")

    message.dynamic_template_data = {'token': token, 'expireDate': date_time}
    message.template_id = template_id
    sendgrid_client = SendGridAPIClient(SENDGRID_API_KEY)
    sendgrid_response = sendgrid_client.send(message)

    return sendgrid_response


def generate_coupon():
    """
    Generate the coupon
    :return: 4 words coupon
    """
    # """"""
    word_file = xp.locate_wordfile()
    my_words = xp.generate_wordlist(wordfile=word_file, min_length=4, max_length=5)
    coupon = xp.generate_xkcdpassword(my_words, numwords=4)
    coupon = '-'.join(coupon.title().split())

    return coupon


def current_time():
    now = datetime.datetime.now()
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    return now


def response_with_status_code(msg, status_code=422, log_msg='true'):
    if status_code != 200:
        logger.error(msg)
    elif log_msg:
        logger.info(msg)
    resp = make_response(msg)
    resp.status_code = status_code

    return resp


def get_access_role(net_id):
    with open(os.path.join(os.path.dirname(__file__), '', 'rbac_config.json')) as json_file:
        access_roles = json.load(json_file)

        if access_roles.get(net_id):
            return access_roles.get(net_id).get("role")
        else:
            logger.warning("This netId doesn't exist on access roles list.")
            return None


def count_list_of_lists(input_lists):
    count = 0
    for listElem in input_lists:
        if type(listElem) is list:
            count += len(listElem)
        else:
            count += 1
    return count


def import_seeds():
    mongo_client = MongoClient(MONGO_URI)
    db = mongo_client[MONGODB_NAME]
    collection = db["SeedReport"]

    filepath = "../../test/test-data/seeds.csv"
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    df = pd.read_csv(file_res)
    for index, row in df.iterrows():
        collection.insert_one(create_seed_report_row(row))
    logger.info(f"Successfully imported {file_res}")


def _create_seed_report_row(csv_row):
    return {
        **{key: value for key, value in csv_row.items() if key in CSV_HEADERS},
        "REPORT_DATE": str(date.today()),
        "STATUS": _get_status(csv_row),
    }


def _get_status(csv_row):
    excluded_email_addresses = {
        "none@email.com",
        "none@emailc.om",
        "none@emil.aom",
        "none@gmail.com",
    }
    should_be_excluded = (
        not csv_row["MYC_VIEWED_DTTM"]
        or not csv_row["EMAIL_ADDRESS"]
        or csv_row["EMAIL_ADDRESS"] in excluded_email_addresses
    )
    return "EXCLUDE" if should_be_excluded else "ELIGIBLE"
