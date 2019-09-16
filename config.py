import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_WEB_URL='https://newsapi.org/v2/sources?/category={}&apiKey={}'
    ARTICLES_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_KEY='2d46df7bd2ef45689ca30c90eadf3061'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}