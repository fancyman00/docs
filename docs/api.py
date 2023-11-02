
from tools.logger import Logger


class DocumentApi:
    def __init__(self, app, route):
        self.logger = Logger(app)

        @app.get(route + '/<id>')
        @self.logger.request_log
        def get(id):
            return "GET " + id

        @app.delete(route + '/<id>')
        @self.logger.request_log
        def delete(id):
            return 'DELETE ' + id

        @app.put(route + '/<id>')
        @self.logger.request_log
        def put(id):
            return 'PUT ' + id

        @app.post(route)
        @self.logger.request_log
        def post():
            return 'POST'
