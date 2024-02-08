from flask_restful import Resource


class HelloWorld(Resource):
    def get(self):
        #Execute SQL query
        return {'hello': 'world'}
    def post(self):
        return {'hello': 'world'}




