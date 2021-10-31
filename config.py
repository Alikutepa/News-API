import os
class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines/sources?&apiKey='
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    @staticmethod
    def init_app(app):
            pass

class ProdConfig(Config):
    '''articles_result = Articles(
                id, author, title, description, url, image, date)
        articles_object.append(articles_result)
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