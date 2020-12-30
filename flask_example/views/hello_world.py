from flask_restful import Resource

from flask_example import app


class HelloWorld(Resource):
    def get(self):
        app.logger.info('hello world requested')
        retvals = {
            "hello": "world",
            "for": "this",
        }

        return retvals, 200


class Hello(Resource):
    def get(self, name):
        return {'hello': name}, 200
