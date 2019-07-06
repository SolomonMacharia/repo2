
import os
basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql://postgres:@localhost/'
database_name = 'questioner'

class Config:
    """ Base configuration """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'some-confidential-string')
    BCRYPT_LOG_ROUNDS = 13

class ProductionConfig(Config):
    """ Production Config """
    DEBUG = False
    SECRET_KEY = 'some-confidential-string'
    DATABASE_URI = 'postgresql:////example'
 
class StagingConfig(Config):
    """ Staging configuration """
    DEVELOPMENT = True

class DevelopmentConfig(Config):
    """Development configuration """
    DEVELOPMENT = True
    DEBUG = True
    DATABASE_URI = os.getenv('DATABASE_URI', postgres_local_base + database_name + '_dev')

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    DATABASE_URI = os.getenv('TEST_DATABASE_URI')