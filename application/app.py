from flask import Flask

from config import ApplicationConfig
from blueprints import root, error_handler, transactions
from middleware import Middleware


def get_application() -> Flask:
    """Creates an application"""

    config = ApplicationConfig()
    app = Flask(__name__)

    app.config.update(**config.dict())
    app.user_config = config

    app.wsgi_app = Middleware(app.wsgi_app)
    return app


app = get_application()

# register blueprints
app.register_blueprint(error_handler, url_prefix="/")
app.register_blueprint(root, url_prefix="/")
app.register_blueprint(transactions, url_prefix="/transactions")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
