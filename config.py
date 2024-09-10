import os

class Config():
    CSRF_ENABLE = True
    SECRET = "DASHBOARD01"
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_FOLDER = os.path.join(os.path.join(ROOT_DIR, 'templates'))
    APP = None
    
class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s/%s' % (IP_HOST, PORT_HOST)  # http://localhost:8000
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://tiago.silva2:de_m7jBG^WZ=@localhost:3306/DASHBOARD ADMINISTRATIVO'
    
app_config = {
    'development': DevelopmentConfig(),
    'testing': None
}

app_active = os.getenv('FLASK_ENV')
if app_active is None:
    app_active = 'development'
    
