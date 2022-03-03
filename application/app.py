from flask import Flask, render_template
from views import usd_view, euro_view, rub_view


def get_application() -> Flask:
    """Method to create an application to manage currency payments"""

    application = Flask(__name__)

    application.register_blueprint(usd_view)
    application.register_blueprint(euro_view)
    application.register_blueprint(rub_view)

    return application


app = get_application()


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


@app.teardown_appcontext
def cleanup(response_or_exception):
    pass


if __name__ == '__main__':
    app.run(host="localhost")
