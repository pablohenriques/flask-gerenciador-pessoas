class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "happy#new*year$21"
    SESSION_COOKIE_SECURE = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///base.db"


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"


class TestingConfig(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False
