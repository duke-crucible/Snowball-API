from flask import current_app as app
from flask import request, session
from requests_oauthlib import OAuth2Session

from app.services import logger


def get_status():
    duke_auth = OAuth2Session(
        client_id=app.config["CLIENT_ID"], redirect_uri=app.config["REDIRECT_URI"]
    )
    authorization_url, state = duke_auth.authorization_url(
        app.config["AUTHORIZATION_URL"]
    )
    logger.debug(f"state: {state}")
    return authorization_url, state


def shib_access():
    auth_state = request.args.get("state")
    # logger.debug("state:" + auth_state)
    duke_auth = OAuth2Session(
        app.config["CLIENT_ID"],
        state=auth_state,
        redirect_uri=app.config["REDIRECT_URI"],
    )

    # token not used so comment out for now
    # token = duke_auth.fetch_token(
    #     app.config["TOKEN_URL"], client_secret=app.config["CLIENT_SECRET"], authorization_response=request.url
    # )
    # option: validate the token

    user_info = duke_auth.get(app.config["USERINFO_URL"]).json()
    logger.debug(user_info)
    # TODO: remove the hook once OAuth is ready
    # net_id = user_info[app.config["AUTH_ID"]]
    net_id = "testGR"

    logger.info("User shibboleth log in netId: " + net_id)
    return net_id


def is_in_session():
    # TODO: need to remove this line once authentication is done
    return True
    if "username" in session:
        logger.info("user is already in session.")
        return True
    else:
        return False


# study Team or Admin
def study_access():
    # TODO: need to remove this line once authentication is done
    return True
    role = user_access_role()
    return True if (role in app.config["STUDY_ACCESS"]) else False


# study Team or Admin
def invite_access():
    role = user_access_role()
    return True if (role in app.config["INVITE_ACCESS"]) else False


# CRC Assistant : C
def crc_assist_access():
    role = user_access_role()
    return True if (role == "C") else False


# study Admin : A
def full_access():
    # TODO: need to remove this line once authentication is done
    return True
    role = user_access_role()
    return True if (role == "A") else False


# data management role : M
def data_extract_access():
    role = user_access_role()
    # logger.info("check if user has data extract access. User's role: " + str(role))
    return True if (role in app.config["EXTRACT_DATA_ACCESS"]) else False


def user_access_role():
    if "role" in session:
        return session["role"]
    else:
        logger.error("user doesn't have a role in session")
        return "N/A"


def get_user_name():
    if "username" in session:
        return session["username"]
    else:
        logger.error("No user in session")
        return "N/A"
