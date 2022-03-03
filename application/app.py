from flask import Flask, render_template

from config import ApplicationConfig
from views import usd_view, euro_view, rub_view


def get_application() -> Flask:
    """Method to create an application to manage currency payments"""

    config = ApplicationConfig()
    app = Flask(__name__)

    app.config.update(**config.dict())

    app.register_blueprint(usd_view)
    app.register_blueprint(euro_view)
    app.register_blueprint(rub_view)

    return app


app = get_application()


@app.errorhandler(404)
def page_not_found(error):
    """Method to handle 404 error"""

    return render_template("404.html")


@app.teardown_appcontext
def cleanup(response_or_exception):
    pass


if __name__ == '__main__':
    app.run(host="localhost")
