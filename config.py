import os

class Config:

     '''
    General configuration parent class
    '''
    QUOTE_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'

    SECRET_KEY = "1234567890"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://christine:bayizere@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
 





 class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'