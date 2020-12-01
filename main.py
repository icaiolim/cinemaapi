from api import app, api, blueprint
from api.config import log
from api.services.hello_service import ns as ns_hello

api.init_app(blueprint)
app.register_blueprint(blueprint)

# Register all routes
api.add_namespace(ns_hello)

log.info('>> CINEMA API http://{}'.format(app.config['SERVER_NAME']))
app.run(debug=True)