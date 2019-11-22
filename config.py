import os

class Config:
    '''
    This is the parent configuration class

    '''

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


config_options = {
'development':DevConfig,
'production':ProdConfig
}