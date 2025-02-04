from flask import Flask
from app.config import Config
from flask_basicauth import BasicAuth

basic_auth = BasicAuth()


def create_app(config_obj=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_obj)

    basic_auth.init_app(app)


    @app.route('/')
    @basic_auth.required
    def index():
        return {"message": "Hello world"}


    return app
