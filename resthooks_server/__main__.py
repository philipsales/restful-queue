from flask import render_template
import connexion

def main():
    app = connexion.App(__name__, specification_dir='./')
    swagger_path='swagger.yml'
    app.add_api('swagger.yml')
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    main()