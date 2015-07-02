import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super secret key'
    CELERY_BROKER_URL = 'redis://localhost:6379',
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'


class DevelopmentConfig(Config):
    DEBUG = True
    WTF_CSRF_ENABLED = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    WTF_CSRF_ENABLED = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
