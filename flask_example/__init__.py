# Flask imports #
# import logging specific settings
import logging
import os
import sys
from logging import DEBUG

from flask import Flask
# FLASK API #
from flask_restful import Api

# we do not have static content be define the path just for sure
app = Flask(__name__, static_url_path='/static')

if os.environ.get('FLASK_SETTINGS'):
    app.config.from_envvar('FLASK_SETTINGS')
else:
    # find env-config/config.py
    from os.path import dirname, join, isfile

    path = dirname(dirname(__file__))
    path = join(path, 'env-config')
    path = join(path, 'config.py')

    if isfile(path):
        app.config.from_pyfile(path)
    else:
        print('PLEASE SET A CONFIG FILE WITH FLASK_SETTINGS OR PUT ONE AT env-config/config.py')
        exit(-1)


# Define handler to use with health probes
@app.route('/healthcheck')
def healthcheck():
    return 'ok'


# define flask api
# Import Flask restful views, make sure these are imported before initializing of the app!!
from flask_example.views.hello_world import HelloWorld, Hello

api = Api(app, default_mediatype='application/json')
api.add_resource(HelloWorld, "/api/hello")
api.add_resource(Hello, "/api/say/<string:name>")


def setup_logging():
    # create root logging
    root = logging.getLogger()
    root.setLevel(app.config.get('LOG_LEVEL', DEBUG))

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

    # initialize the Flask logger (removes all handlers)
    _ = app.logger
    app.logger.setLevel(app.config.get('LOG_LEVEL', DEBUG))
    app.logger.addHandler(handler)


setup_logging()
