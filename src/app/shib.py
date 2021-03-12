from requests_oauthlib import OAuth2Session
from flask import request, session
from src.app.config import *


def get_status():
    duke_auth = OAuth2Session(client_id=CLIENT_ID, redirect_uri=REDIRECT_URI)
    authorization_url, state = duke_auth.authorization_url(AUTHORIZATION_URL)
    return authorization_url, state


def shib_access():
    auth_state = request.args.get('state')
    # logger.debug("state:" + auth_state)
    duke_auth = OAuth2Session(CLIENT_ID, state=auth_state, redirect_uri=REDIRECT_URI)

    token = duke_auth.fetch_token(TOKEN_URL, client_secret=CLIENT_SECRET, authorization_response=request.url)
    # option: validate the token

    user_info = duke_auth.get(USERINFO_URL).json()
    net_id = user_info[AUTH_ID]

    logger.info("User shibboleth log in netId: " + net_id)
    return net_id


def is_in_session():
    if 'username' in session:
        logger.info("user is already in session.")
        return True
    else:
        return False


# study Team or Admin
def study_access():
    role = user_access_role()
    return True if (role in STUDY_ACCESS) else False


# study Team or Admin
def invite_access():
    role = user_access_role()
    return True if (role in INVITE_ACCESS) else False


# CRC Assistant : C
def crc_assist_access():
    role = user_access_role()
    return True if (role == 'C') else False


# CRC Assistant : C
def crc_assist_access():
    role = user_access_role()
    return True if (role == 'C') else False


# study Admin : A
def full_access():
    role = user_access_role()
    return True if (role == 'A') else False


# data management role : M
def data_extract_access():
    role = user_access_role()
    # logger.info("check if user has data extract access. User's role: " + str(role))
    return True if (role in EXTRACT_DATA_ACCESS) else False


def user_access_role():
    if 'role' in session:
        return session['role']
    else:
        logger.error("user doesn't have a role in session")
        return 'N/A'
