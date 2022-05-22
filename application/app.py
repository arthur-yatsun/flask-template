from flask import Flask

from config import ApplicationConfig
from blueprints import root, error_handler, transactions


def get_application() -> Flask:
    """Creates an application"""

    config = ApplicationConfig()
    app = Flask(__name__)

    app.config.update(**config.dict())
    app.user_config = config
    return app


app = get_application()

# register blueprints
app.register_blueprint(error_handler, url_prefix="/")
app.register_blueprint(root, url_prefix="/")
app.register_blueprint(transactions, url_prefix="/transactions")


if __name__ == '__main__':
    app.run(host="localhost")
