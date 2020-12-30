#!/usr/bin/env python

from flask_script import Command, Option, Manager

try:
    from gunicorn.app.base import Application

    GUNICORN = True
except ImportError:
    # Gunicorn does not yet support Windows.
    # For dev on Windows, make this an optional import.
    print('Could not import gunicorn, skipping.')
    GUNICORN = False

from flask_example import app

manager = Manager(app)


class APIServer(Command):

    def __init__(self, host='0.0.0.0', port=app.config.get('API_PORT'), workers=app.config.get('WORKERS')):
        self.address = "{}:{}".format(host, port)
        self.workers = workers

    def get_options(self):
        return (
            Option('-b', '--bind',
                   dest='address',
                   type=str,
                   default=self.address),
            Option('-w', '--workers',
                   dest='workers',
                   type=int,
                   default=self.workers),
        )

    def run(self, *args, **kwargs):

        workers = kwargs['workers']
        address = kwargs['address']

        if not GUNICORN:
            print('GUNICORN not installed. Try `runserver` to use the Flask debug server instead.')

        else:
            class FlaskApplication(Application):
                def init(self, parser, opts, args):
                    return {
                        'bind': address,
                        'workers': workers,
                        'timeout': 1800
                    }

                def load(self):
                    return app

            FlaskApplication().run()


def main():
    manager.add_command("run_api_server", APIServer())
    manager.run()


if __name__ == '__main__':
    main()
