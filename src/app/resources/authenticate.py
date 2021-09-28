from flask import current_app as app
from flask import redirect, render_template, session, url_for
from flask_restful import Resource

from app.services import logger
from app.shib import shib_access
from app.utils import get_access_role, oauth_authentication


class Login(Resource):
    def get(self):
        return oauth_authentication()


class Logout(Resource):
    def get(self):
        session.clear()
        return app.send_static_file("logout.html")


class CallBack(Resource):
    def get(self):
        net_id = shib_access()
        logger.info("OAuth login with net_id: " + net_id)

        # optional: validate/ introspect the token
        # check if the user netID is authorized to snowball

        user_role = get_access_role(net_id)

        if user_role is None:
            return render_template("unauthorized.html")
        else:
            logger.info(
                "user: "
                + net_id
                + " has been granted to access snowball with role: "
                + user_role
            )
            session["role"] = user_role
            session["username"] = net_id
            logger.info("redirect to homepage")
            return redirect(url_for("homepage"))
