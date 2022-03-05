from flask import Flask, render_template

from config import ApplicationConfig
from views import transactions


def get_application() -> Flask:
    """Method to create an application to manage currency payments"""

    config = ApplicationConfig()
    app = Flask(__name__)
    app.config.update(**config.dict())

    return app


app = get_application()

# register blueprints
app.register_blueprint(transactions, url_prefix="/")


@app.errorhandler(404)
def page_not_found(error):
    """Handles 404 error"""

    return render_template("404.html")


if __name__ == '__main__':
    app.run(host="localhost")
