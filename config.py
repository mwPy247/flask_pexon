""" The module provides configuration classes to be used by the app object. """


class BaseConfig(object):
    """ Base Configuration to be inherited by all configuration classes. """
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Because of Deprecation Warning


class Test(BaseConfig):
    """ Configuration for a testing environment with an in-memory sqlite database. """
    DEBUG = True
    TESTING = True
    DB_SERVER = 'localhost'
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class Dev(BaseConfig):
    """ Configuration for a development environment with a file-based sqlite database. """
    DEBUG = False
    TESTING = False
    DB_SERVER = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/movies.sqlite'
