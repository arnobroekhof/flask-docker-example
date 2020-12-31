# some config file
import os
API_PORT = os.getenv('API_PORT', default=8080)
LOG_LEVEL = os.getenv('LOG_LEVEL', default='INFO')
WORKERS = os.getenv('WORKERS', default=4)
