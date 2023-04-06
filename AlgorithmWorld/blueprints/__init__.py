from AlgorithmWorld.blueprints.user import user_bp
from AlgorithmWorld.blueprints.file import file_bp


def register_blueprints(app):
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(file_bp, url_prefix='/file')
