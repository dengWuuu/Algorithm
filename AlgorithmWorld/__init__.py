from flask import Flask

from AlgorithmWorld.config.config import config
from AlgorithmWorld.extensions import db


def create_app(config_name=None):
    if config_name is None: config_name = 'production'
    app = Flask('AlgorithmWorld')
    # 处理中文编码
    app.config['JSON_AS_ASCII'] = False
    app.config.from_object(config[config_name])
    register_extensions(app)

    return app


def register_extensions(app):
    db.init_app(app)

# def register_blueprints(app):
