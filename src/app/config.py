import os

from dotenv import load_dotenv


class DefaultConfig(object):
    DEBUG = True

    # Load .env for local development
    load_dotenv()

    APP_ENV = os.environ.get("SERVICE_APP_ENV", "local")

    SESSION_KEY = os.environ["SERVICE_SESSION_KEY"]
    # CLIENT_SECRET = os.environ["CLIENT_SECRET"]
    CLIENT_ID = os.getenv("SERVICE_DUKE_CLIENT_ID", "snowball_web_test")

    BASE_URI = os.getenv("SERVICE_BASE_URI", "http://localhost:5000")

    # Mongo Settings
    MONGO_URI = os.environ["SERVICE_MONGODB_URI"]
    MONGODB_NAME = os.environ["SERVICE_DB_NAME"]
    MAX_SERVER_SEL_DELAY = 10000  # 10000ms as maximum server selection delay
    COLLECTIONS = {
        "seeds": "Seeds",
        "participants": "Participants",
        "consent": "Consent",
        "survey": "Surveys",
        "consentform": "ConsentForm",
    }

    # Lifetime of token (in days) for various states throughout the process
    TTLD_GENERATION_TO_CONSENT = os.getenv("TTLD_GENERATION_TO_CONSENT", "4")
    TTLD_CONSENT_TO_SURVEY_COMPLETION = os.getenv(
        "TTLD_CONSENT_TO_SURVEY_COMPLETION", "2"
    )
    TTLD_SURVEY_COMPLETION_TO_SCHEDULED_TEST = os.getenv(
        "TTLD_SURVEY_COMPLETION_TO_SCHEDULED_TEST", "2"
    )
    TTLD_TEST_RESULT = 99999

    # Email Settings
    SNOWBALL_EMAIL = "snowball@duke.edu"
    SENDGRID_API_KEY = os.getenv("SERVICE_SENDGRID_API_KEY")
    SENDGRID_URL = os.getenv("SENDGRID_URL", "https://api.sendgrid.com/v3/mail/send")
    SENDGRID_FROM_ADDRESS = os.getenv("SENDGRID_FROM_ADDRESS", "snowball@duke.edu")
    SENDGRID_SEED_TEMPLATE = os.getenv(
        "SENDGRID_INVITE_TEMPLATE", "d-c9e655c0b9a7439ca654f9791eb09dc0"
    )
    SENDGRID_PEER_TEMPLATE = os.getenv(
        "SENDGRID_PEER_TEMPLATE", "d-6e82e76a1fb543ef95821656accb5480"
    )

    # SMS Settings
    SMS_PHONE_NUMBER = os.getenv("SERVICE_COMMUNICATION_PHONE_NUMBER")
    SMS_CONNECTION_STRING = os.getenv("SERVICE_COMMUNICATION_CONNECTION_STRING")

    # P for prod, D for dev
    ENV = ["P", "D"]

    # Roles for access
    # A for Study Admin, L for Lab Personnel, M for data management, T for study team, V for visitor
    ROLES = ["A", "L", "M", "T", "V"]
    # roles access levels are kept here:
    # https://app.smartsheet.com/sheets/5f7wFr79GW6pv27ghgvq86rjr6PXxx2fxf3XQWR1?view=grid
    STUDY_ACCESS = ["A", "T"]
    INVITE_ACCESS = ["A", "T", "C"]
    EXTRACT_DATA_ACCESS = ["A", "M"]

    # Field definitions to avoid typo
    PAT_NAME = "PAT_NAME"
    PAT_AGE = "PAT_AGE"
    PAT_SEX = "PAT_SEX"
    ETHNIC_GROUP = "ETHNIC_GROUP"
    EMAIL_ADDRESS = "EMAIL_ADDRESS"
    ALTER_EMAIL = "ALTERNATIVE_EMAIL"
    MOBILE_NUM = "MOBILE_NUM"
    HOME_NUM = "HOME_NUM"
    PREFERRED_COMM = "PREFERRED_COMMUNICATION"
    PARTICIPANT_TOKEN = "COUPON"
    STATUS_LOG = "STATUS_CHANGE_LOG"
    RESULT_DATE = "RESULT_DATE"
    REPORT_DATE = "REPORT_DATE"
    TEST_RESULT = "TEST_RESULT"
    TEST_DATE = "TEST_DATE"
    RESULT_NOTIFIED = "RESULT_NOTIFIED"
    RECORD_ID = "RECORD_ID"
    COUPON_ISSUE_DATE = "COUPON_ISSUE_DATE"
    COUPON_REDEEM_DATE = "COUPON_REDEEM_DATE"
    CONSENT_DATE = "CONSENT_DATE"
    SURVEY_COMPLETION_DATE = "SURVEY_COMPLETION_DATE"
    ENROLLMENT_COMPLETED = "ENROLLMENT_COMPLETED_DATE"
    PEER_COUPON_NUM = "NUM_COUPONS"
    PARENT_RECORD_ID = "PARENT_RECORD_ID"
    PEER_COUPONS_SENT = "COUPON_SENT"
    PEER_COUPONS_LIST = "peer-coupons"
    CREATED_AT = "CREATED_AT"
    UPDATED_AT = "UPDATED_AT"

    TEST_RESULT_DATE_FORMAT_ADD = "%m-%d-%Y%H:%M"
    TEST_RESULT_DATE_FORMAT_CSV = "%m/%d/%y %H:%M"

    SEED_STATUS_LIST = [
        "INCLUDE",
        "EXCLUDE",
        "DEFER",
        "ELIGIBLE",
    ]
    # Fields to index
    SEEDS_INDEXES = [
        REPORT_DATE,
        "MRN",
        "STATUS",
        PAT_NAME,
        PAT_AGE,
        PAT_SEX,
        ETHNIC_GROUP,
        "RACE",
        "ZIP",
        RESULT_DATE,
        CREATED_AT,
    ]
    PARTICIPANTS_INDEXES = [
        "MRN",
        "STATUS",
        PAT_NAME,
        PAT_AGE,
        PAT_SEX,
        ETHNIC_GROUP,
        "RACE",
        "ZIP",
        RECORD_ID,
        COUPON_ISSUE_DATE,
        COUPON_REDEEM_DATE,
        CONSENT_DATE,
        SURVEY_COMPLETION_DATE,
        CREATED_AT,
        TEST_DATE,
    ]
    CONSENT_FORM_INDEXES = [
        "version",
        "modifier",
        "uploadDate",
    ]
    CONSENT_INDEXES = {
        CREATED_AT,
    }
    SURVEY_INDEXES = {
        CREATED_AT,
    }
    COLLECTION_INDEXES = {
        "Seeds": SEEDS_INDEXES,
        "Participants": PARTICIPANTS_INDEXES,
        "ConsentForm.files": CONSENT_FORM_INDEXES,
        "Consent": CONSENT_INDEXES,
        "Surveys": SURVEY_INDEXES,
    }

    # MC seeds report columns and fields
    COMM_FIELDS = {
        EMAIL_ADDRESS: 1,
        MOBILE_NUM: 1,
        PREFERRED_COMM: 1,
        "_id": 0,
    }
    # Fields to extract from mongodb
    SEED_REPORT_FIELDS = {
        "STATUS": 1,
        "MRN": 1,
        EMAIL_ADDRESS: 1,
        MOBILE_NUM: 1,
        # "ZIP": 1,
        TEST_RESULT: 1,
        RESULT_DATE: 1,
        HOME_NUM: 1,
        PAT_AGE: 1,
        PAT_SEX: 1,
        "RACE": 1,
        ETHNIC_GROUP: 1,
        REPORT_DATE: 1,
        "_id": 0,
    }
    COHORT_REPORT_FIELDS = {
        "MRN": 1,
        PAT_NAME: 1,
        PAT_AGE: 1,
        PAT_SEX: 1,
        "RACE": 1,
        ETHNIC_GROUP: 1,
        EMAIL_ADDRESS: 1,
        MOBILE_NUM: 1,
        HOME_NUM: 1,
        PREFERRED_COMM: 1,
        "LANGUAGE": 1,
        "ZIP": 1,
        TEST_RESULT: 1,
        RESULT_DATE: 1,
        REPORT_DATE: 1,
        "STATUS": 1,
        RECORD_ID: 1,
        PARTICIPANT_TOKEN: 1,
        "FIRST_NAME": 1,
        "LAST_NAME": 1,
        COUPON_ISSUE_DATE: 1,
        COUPON_REDEEM_DATE: 1,
        CONSENT_DATE: 1,
        SURVEY_COMPLETION_DATE: 1,
        ENROLLMENT_COMPLETED: 1,
        "PTYPE": 1,
        PARENT_RECORD_ID: 1,
        PEER_COUPONS_LIST: 1,
        "_id": 0,
    }
    # fields for coupon redeem page
    FIELDS_FOR_COUPON_REDEEM_PAGE = {
        "_id": 0,
        RECORD_ID: 1,
        "FIRST_NAME": 1,
        "LAST_NAME": 1,
        "ZIP": 1,
        MOBILE_NUM: 1,
        HOME_NUM: 1,
        EMAIL_ADDRESS: 1,
        "PTYPE": 1,
        SURVEY_COMPLETION_DATE: 1,
        ENROLLMENT_COMPLETED: 1,
    }
    # fields for peer coupon distribution page
    FIELDS_FOR_PEER_COUPON_PAGE = {
        "_id": 0,
        RECORD_ID: 1,
        "FIRST_NAME": 1,
        "LAST_NAME": 1,
        MOBILE_NUM: 1,
        ALTER_EMAIL: 1,
        EMAIL_ADDRESS: 1,
        PEER_COUPON_NUM: 1,
        PEER_COUPONS_SENT: 1,
        COUPON_ISSUE_DATE: 1,
        COUPON_REDEEM_DATE: 1,
        CONSENT_DATE: 1,
        SURVEY_COMPLETION_DATE: 1,
        "contacts": 1,
    }
    # fields for invite peer
    FIELDS_FOR_INVITE_PEER = {
        "_id": 0,
        RECORD_ID: 1,
        MOBILE_NUM: 1,
        ALTER_EMAIL: 1,
        EMAIL_ADDRESS: 1,
        PEER_COUPON_NUM: 1,
        PEER_COUPONS_LIST: 1,
        PEER_COUPONS_SENT: 1,
    }
    #  fields for test schedule page
    FIELDS_FOR_TEST_SCHEDULE_PAGE = {
        "_id": 0,
        RECORD_ID: 1,
        "FIRST_NAME": 1,
        "LAST_NAME": 1,
        MOBILE_NUM: 1,
        PAT_AGE: 1,
        "PTYPE": 1,
        PARTICIPANT_TOKEN: 1,
        TEST_RESULT: 1,
        TEST_DATE: 1,
        RESULT_DATE: 1,
        RESULT_NOTIFIED: 1,
    }
    # fields to be copied from seeds to participants
    FIELDS_FROM_SEEDS_TO_PARTICIPANT = {
        "MRN": 1,
        PAT_NAME: 1,
        PAT_AGE: 1,
        PAT_SEX: 1,
        "RACE": 1,
        ETHNIC_GROUP: 1,
        EMAIL_ADDRESS: 1,
        MOBILE_NUM: 1,
        HOME_NUM: 1,
        PREFERRED_COMM: 1,
        "LANGUAGE": 1,
        "ZIP": 1,
        TEST_RESULT: 1,
        RESULT_DATE: 1,
        REPORT_DATE: 1,
        # "ADD_LINE_1": 1,
        # "CITY": 1,
        # "STATE": 1,
        "STATUS": 1,
        STATUS_LOG: 1,
        "_id": 0,
    }
    CRM_FIELD = {
        "comments": 1,
        "_id": 0,
    }

    # unauthorized response:
    UNAUTHORIZED_MESSAGE = 'Error 403: You do not have permission to access this information. If you believe you have \
    received this notification in error, please contact the \
    < a href = "https://app.smartsheet.com/b/form/a0871a8eb325405fae818df814018099" \
    target="_blank">system administrator</a>'


class LocalConfig(DefaultConfig):
    # Note: assume docker compose is used to bring up local env, otherwise use .env
    pass


class DevelopConfig(DefaultConfig):
    # SMS Settings
    # TODO: get application id from variable by env
    SMS_MESSAGE_TYPE = "TRANSACTIONAL"
    # TODO: finalize this
    ORIGINATION_NUMBER = "+14243961101"
    SMS_SENDER_ID = "snowballsms"
    REGION = "us-east-1"


class TestConfig(DefaultConfig):
    # TODO: for now use local mongodb brought up by docker compose, later may change to a fixed ip
    # MONGO_URI = "mongodb://root:localdev@snowballgr-db:27017/?ssl=false"
    MONGODB_NAME = "test"


class ProdConfig(DefaultConfig):
    DEBUG = False


CONFIGURATIONS = {
    "local": LocalConfig,
    "dev": DevelopConfig,
    "test": TestConfig,
    "prod": ProdConfig,
}
