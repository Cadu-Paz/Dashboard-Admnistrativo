from flask import Flask
from admin.Admin import start_views
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

# Inicializa a instância do banco de dados fora da função create_app
db = SQLAlchemy()

def create_app(config):
    app = Flask(__name__)

    app.secret_key = config.SECRET
    app.config.from_object(config)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['FLASK_ADMIN_SWATCH'] = 'paper'  # Admin

    # Chama a função para iniciar as views do admin
    start_views(app, db)  # Admin
    Bootstrap(app)  # Admin

    # Adiciona as configurações após a inicialização
    config.APP = app

    # Inicializa o banco de dados com a app
    db.init_app(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def index():
        return 'oi'

    return app  # Retorna a instância da aplicação
