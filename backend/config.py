


class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///security.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    APPLICATION_ROOT = '/api'
    DATABASE_DROP_CREATE_ALL = True
    POPULATE_WITH_FIXTURES = True
    DEBUG = True


def get_config():
    return 'config.Config'