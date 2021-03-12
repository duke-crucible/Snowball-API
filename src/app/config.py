from dotenv import load_dotenv
import os, sys
import logging

# Load .env for local development
load_dotenv()

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger("Snowball_GR")

SESSION_KEY = os.environ['SESSION_KEY']

# shibboleth & role based access control
AUTHORIZATION_URL = 'https://oauth.oit.duke.edu/oidc/authorize'
TOKEN_URL = 'https://oauth.oit.duke.edu/oidc/token'
USERINFO_URL = 'https://oauth.oit.duke.edu/oidc/userinfo'
BASE_URI = os.getenv('BASE_URI', 'http://localhost:8000')
CLIENT_ID = os.getenv('CLIENT_ID', 'snowball_web_test')
CLIENT_SECRET = os.environ['CLIENT_SECRET']
AUTH_ID = 'dukeNetID'
CALL_BACK_URI='/auth/callback'
REDIRECT_URI = BASE_URI + CALL_BACK_URI

# # Mongo Settings
MONGO_URI = os.environ['MONGODB_URI']
MONGODB_NAME = os.environ['MONGODB_NAME']
MAX_SERVER_SEL_DELAY = 10000  # 10000ms as maximum server selection delay

# P for prod, D for dev
ENV = ["P", "D"]                     

# Roles for access
ROLES = ["A", "L", "M", "T", "V"]    # A for Study Admin, L for Lab Personnel, M for data management, T for study team, V for visitor
# roles access levels are kept here: https://app.smartsheet.com/sheets/5f7wFr79GW6pv27ghgvq86rjr6PXxx2fxf3XQWR1?view=grid
STUDY_ACCESS = ['A', 'T']
INVITE_ACCESS = ['A', 'T', 'C']
EXTRACT_DATA_ACCESS = ['A', 'M']

# MC seeds report columns and fields
EMAIL_ADDRESS_FIELD = {"EMAIL_ADDRESS": 1, "_id": 0}
STATUS_FIELD = {"STATUS": 1, "_id": 0}
MYC_VIEWED_DTTM = "MYC_VIEWED_DTTM"
EMAIL_ADDRESS = "EMAIL_ADDRESS"
INCLUDE_STATUS = "INCLUDE"
DAILY_REPORT_FIELDS = {"STATUS": 1, "MRN": 1, "I/E_STATUS": 1, "PAT_AGE": 1, "PAT_SEX": 1, "RACE": 1, "ETHNIC_GROUP": 1, "ZIP": 1, "RESULT_DATE": 1, "_id": 0 }
FULL_REPORT_FIELDS = {"STATUS": 1, "MRN": 1, "PAT_NAME": 1, "PAT_AGE": 1, "PAT_SEX": 1, "RACE": 1, "ETHNIC_GROUP": 1, "LANGUAGE": 1,	"EMAIL_ADDRESS": 1,
                      "MOBILE_NUM": 1,	"HOME_NUM": 1, "ADD_LINE_1": 1, "CITY": 1, "STATE": 1, "ZIP": 1, "ORDER_TYPE": 1, "TEST_NAME": 1, "TEST_RESULT": 1,
                      "SPECIMN_TAKEN_DATE": 1,	"SPECIMEN_SOURCE": 1, "SPECIMEN_TYPE": 1, "RESULT_DATE": 1, "ORDER_CLASS": 1,  "MYC_VIEWED_DTTM": 1, "_id": 0 }
# "MYC_RELEASE_DTTM": 1, "MYC_VIEWED_DTTM": 1, "PAT_ENC_CSN_ID": 1, "ENC_TYPE": 1,	"PRC_NAME": 1, "ED_DISPOSITION": 1, "APPT_TIME": 1,
# "HOSP_ADMSN_TIME": 1,	"HOSP_DISCH_TIME": 1, "DEPARTMENT": 1,

# data extract fields
DATA_EXTRACT_FIELDS = {"record_id": 1, "redeemed_token": 1, "participant_type": 1, "date_created": 1, "generated_tokens": 1, "_id": 0}

# coupon status report fields
INVITATION_FIELDS = {"invite_token":1, "to_email":1, "date_created":1}
CONTACT_FIELDS = {"MRN": 1, "PAT_NAME": 1, "LANGUAGE": 1, "EMAIL_ADDRESS": 1, "MOBILE_NUM": 1, "HOME_NUM": 1, "TEST_RESULT": 1, "RESULT_DATE": 1, "_id": 0 }

# main daily report query
MAIN_REPORT_QUERY = {"STATUS": "ELIGIBLE"}

# exclude report MongoDb queries
EXCLUDE_REPORT_QUERY = {"$or": [
    {"STATUS": "EXCLUDE"},
    {"STATUS": "DEFER"}
]
}

DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
# unauthorized response:
UNAUTHORIZED_MESSAGE = 'Error 403: You do not have permission to access this information. If you believe you have received this notification in error, please contact the <a href="https://app.smartsheet.com/b/form/a0871a8eb325405fae818df814018099" target="_blank">system administrator</a>'