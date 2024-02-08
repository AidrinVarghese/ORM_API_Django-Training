from flask_restful import Resource

class Messages(Resource):
    def get(self, id):
        return {'message': 'successfully sent'}