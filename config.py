import os

class Config:
    '''
    This is the parent configuration class

    '''
    SECRET_KEY = "dfghjxfghjertyui45679dfhj"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nyakinyua:Lastman@localhost/pitches'
class ProdConfig(Config):
    '''
     production configuration class which is a child of config class
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration class, child of the class Config
    '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nyakinyua:Lastman@localhost/pitches'


config_options = {
'development':DevConfig,
'production':ProdConfig
}