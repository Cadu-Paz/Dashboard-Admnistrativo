import os

class Config:
    CSRF_ENABLED = True  # Se estiver usando Flask-WTF, ajuste o nome
    SECRET = os.getenv("FLASK_SECRET", "DASHBOARD01")  # Use variável de ambiente
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_FOLDER = os.path.join(ROOT_DIR, 'templates')  # Diretório de templates
    APP = None  # Pode ser removido se não for necessário

class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:KduCDA#31@localhost:3306/dashboard_admnistrativo'
    
    @property
    def URL_MAIN(self):
        return f'http://{self.IP_HOST}:{self.PORT_HOST}'  # Usar método de instância

app_config = {
    'development': DevelopmentConfig(),
    'testing': None  # Defina uma configuração de teste, se necessário
}

app_active = os.getenv('FLASK_ENV', 'development')  # Atribui 'development' se não estiver definida
