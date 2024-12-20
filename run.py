from config import app_config, app_active
from app import create_app, db  # Certifique-se de importar db

# Configuração ativa
config = app_config[app_active]

# Cria a aplicação passando a configuração correta
app = create_app(config)

with app.app_context():
    db.create_all()  # Cria todas as tabelas definidas nos modelos

if __name__ == '__main__':
    # Executa a aplicação Flask com as configurações
    app.run(host=config.IP_HOST, port=config.PORT_HOST)
