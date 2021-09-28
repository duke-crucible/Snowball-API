from base64 import b64encode

from flask import make_response, request
from flask_restful import Resource

from app import db_utils, status, utils
from app.services import logger


class ConsentForm(Resource):
    def post(self):
        logger.debug(request.files)
        logger.debug(request.form)
        if "comments" in request.form:
            comments = request.form.get("comments")
            logger.debug(f"comments: {comments}")
        else:
            comments = "N/A"
            logger.error("No comments provided")
        file = request.files["form"]
        try:
            version = db_utils.save_new_consent_form(file, comments, "N/A")
            return utils.response_with_status_code(
                f"Successfully saved new version ({version}) of consent form into db",
                status.HTTP_200_OK,
            )
        except Exception as err:
            return utils.response_with_status_code(
                f"Failed to save new version ({version}) of consent form into db: {str(err)}"
            )

    def get(self):
        try:
            consent = db_utils.get_latest_consent_form()
            logger.info(f"comments: {consent.comments}, modifier: {consent.modifier}")
            dict = {
                "version": consent.version,
                "uploadDate": consent.uploadDate,
                "form": b64encode(consent.read()).decode("utf-8"),
            }
            logger.debug(
                "Successfully retrieved version "
                + str(dict["version"])
                + " consent form uploaded on "
                + str(dict["uploadDate"])
            )
            response = make_response(dict)
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as err:
            logger.debug(err)
            error_msg = f"Failed to retrieve latest consent document: {str(err)}"
            logger.error(error_msg)
            return utils.response_with_status_code(error_msg)
