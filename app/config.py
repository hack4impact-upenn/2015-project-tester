import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super secret key'
    CELERY_BROKER_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL') or 'redis://localhost:6379'
    CELERY_REDIS_MAX_CONNECTIONS = 5


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
