
class Config(object):
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:groot@localhost:5432/groot'
    SECRET_KEY='secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True