from flask import Blueprint, render_template
from http import HTTPStatus

error_handler = Blueprint("error_handler", __name__)


@error_handler.app_errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error):
    """Handles 404 error"""

    return render_template("errors/404.html")


@error_handler.app_errorhandler(HTTPStatus.METHOD_NOT_ALLOWED)
def page_not_found(error):
    """Handles 405 error"""

    return render_template("errors/405.html")


@error_handler.app_errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def server_internal_error(error):
    """Handles 500 error"""

    # Houston, we have a problem
