from api import app, api, blueprint
from api.config import log
from api.services.hello_service import ns as ns_hello
from api.services.genero_service import ns as ns_genero
from api.services.filme_service import ns as ns_filme

api.init_app(blueprint)
app.register_blueprint(blueprint)

# Register all routes
api.add_namespace(ns_hello)
api.add_namespace(ns_genero)
api.add_namespace(ns_filme)

log.info('>> CINEMA API http://{}'.format(app.config['SERVER_NAME']))
app.run(debug=True)