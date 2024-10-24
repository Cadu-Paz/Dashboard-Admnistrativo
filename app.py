from flask import Flask
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap  # Corrigido: use o Bootstrap do flask_bootstrap
from flask_sqlalchemy import SQLAlchemy

from admin.Admin import start_views  # Certifique-se de que este caminho está correto

# Inicializa o banco de dados e o Migrate
db = SQLAlchemy()  # Corrigido: inicializa o objeto db
migrate = Migrate()

def create_app(config):
    app = Flask(__name__)

    # Configurações da aplicação
    app.secret_key = config.SECRET
    app.config.from_object(config)

    # Configura o URI do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_ADMIN_SWATCH'] = 'paper'

    # Inicializa o banco de dados e outras extensões
    db.init_app(app)  # Corrigido: inicializar o banco de dados com a app
    migrate.init_app(app, db)  # Inicializa o Migrate com a app e o db
    start_views(app, db)  # Registra as views
    Bootstrap(app)  # Corrigido: inicializa o Bootstrap

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def index():
        return 'Faculdade Impacta -- dashboard administrativo ADS 5A manhã.'

    return app
