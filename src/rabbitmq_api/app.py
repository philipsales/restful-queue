import flask 
import connexion

from configuration.base_conf import api_config

conn = api_config.ApiConfig[api_config.ApiENV]

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    swagger_path='swagger.yml'
    app.add_api('swagger.yml')
    app.run(host=conn['HOST'], port=conn['PORT'], debug=conn['DEBUG'])

if __name__ == '__main__':
    main()
