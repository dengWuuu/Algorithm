class BaseConfig(object):
    SECRET_KEY = "dev key"


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Aa1076766987@127.0.0.1:3306/AlgorithmWorld?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Aa1076766987@127.0.0.1:3306/AlgorithmWorld?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Aa1076766987@127.0.0.1:3306/AlgorithmWorld?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
