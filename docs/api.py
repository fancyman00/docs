
from tools.logger import Logger


class DocumentApi:
    def __init__(self, app, route):
        self.logger = Logger(app)

        @app.get(route + '/<id>')
        @self.logger.request_log('Получение документа')
        def get(id):
            return "GET " + id

        @app.delete(route + '/<id>')
        @self.logger.request_log('Удаление документа')
        def delete(id):
            return 'DELETE ' + id

        @app.put(route + '/<id>')
        @self.logger.request_log('Изменение документа')
        def put(id):
            return 'PUT ' + id

        @app.post(route)
        @self.logger.request_log('Добавление документа')
        def post():
            return 'POST'
