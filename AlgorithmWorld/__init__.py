from flask import Flask

from AlgorithmWorld.blueprints import register_blueprints
from AlgorithmWorld.config.config import config
from AlgorithmWorld.extensions import db
from AlgorithmWorld.utils.jwtUtils import jwt_authentication


def create_app(config_name=None):
    if config_name is None:
        config_name = 'production'
    app = Flask('AlgorithmWorld')
    # 处理中文编码
    app.config['JSON_AS_ASCII'] = False
    app.config.from_object(config[config_name])

    # 跨域支持
    app.after_request(after_request)

    register_extensions(app)
    register_blueprints(app)

    jwt_init(app)
    return app


def register_extensions(app):
    db.init_app(app)


def jwt_init(app):
    app.before_request(jwt_authentication)


# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
