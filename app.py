from flask import Flask, request, Response
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap  
from flask_sqlalchemy import SQLAlchemy
import json

from admin.Admin import start_views  

# Inicializa o banco de dados e o Migrate
db = SQLAlchemy()  
migrate = Migrate()

def create_app(config):
    app = Flask(__name__)

    # Configurações da aplicação
    app.secret_key = config.SECRET
    app.config.from_object(config)
    app.config.from_pyfile('config.py')
    # Configura o URI do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_ADMIN_SWATCH'] = 'paper'

    # Inicializa o banco de dados e outras extensões
    db.init_app(app)  
    migrate.init_app(app, db)  # Inicializa o Migrate com a app e o db
    start_views(app, db)  # Registra as views
    Bootstrap(app) 

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/report', methods=['POST'])
    def report():
        state = request.form['state']
        disease = request.form['disease']
        
        patients = ctrl.reportByState(state, disease)
        return Response(json.dumps({}, ensure_ascii=False), mimetype='application/json'), 200, {}
    return app
