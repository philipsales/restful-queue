import flask 
import connexion
import logs.logging_conf, logging
from configuration.base_conf import api_config

logger = logging.getLogger("app.py")
conn = api_config.ApiConfig[api_config.ApiENV]

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    swagger_path='swagger.yml'
    app.add_api('swagger.yml')
    app.run(host=conn['HOST'], port=conn['PORT'], debug=conn['DEBUG'])

if __name__ == '__main__':
    main()
