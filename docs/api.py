import json

from flask import Response

from docs.controller import DocumentController
from tools.logger import Logger


class DocumentApi:
    def __init__(self, app, route, db):
        self.logger = Logger(app)
        self.controller = DocumentController(db)

        @app.get(route + '/<id>')
        @self.logger.request_log('Получение документа')
        def get(id):
            body = None
            if id == 0:
                body = self.controller.get_all_documents()
            else:
                body = self.controller.get_document(id)
            return json.dumps(body)

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
            return self.controller.create_document()
