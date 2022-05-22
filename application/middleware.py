from werkzeug import Request


class Middleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)

        print(f"{request.path = }, {request.url = }")

        return self.app(environ, start_response)
