import logging

#
# APPLICATION
#
def configure_app(app):
    app.config['SERVER_NAME'] = '127.0.0.1:5600'
    app.config['FLASK_DEBUG'] = 'True'
    app.config['JSON_AS_ASCII'] = 'False'


#
# RESTX + SWAGGER
#
def configure_restx(app):
    app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'
    app.config['RESTPLUS_VALIDATE'] = True
    app.config['RESTPLUS_MASK_SWAGGER'] = False
    app.config['ERROR_404_HELP'] = False

#
# PostgreSQL
#
def configurar_database(app,db):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://caio:admin@localhost:5432/LIVRARIA'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    db.init_app(app)
    db.create_all(app=app)

#
# LOG
#
def configure_log():
    logging.basicConfig(level=logging.INFO)
    handler = logging.FileHandler("cinema-api.log")
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.INFO)
    log.addHandler(handler)
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    log.addHandler(handler)
    return log

log = configure_log()