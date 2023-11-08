import json

from flask import request

from docs.controller import DocumentController
from tools.logger import Logger
from tools.request import required_payload


class DocumentApi:
    def __init__(self, app, route, db):
        self.logger = Logger(app)
        self.controller = DocumentController(db)

        @app.get(route + '/<id>')
        @self.logger.request_log('Получение документа')
        def get(id):
            body = self.controller.get_document(id)
            return json.dumps(body)

        @app.get(route)
        @self.logger.request_log('Получение документов')
        def get_all():
            count = request.args.get('count')
            body = self.controller.get_all_documents(count)
            return json.dumps(body)

        @app.delete(route + '/<id>')
        @self.logger.request_log('Удаление документа')
        def delete(id):
            return 'DELETE ' + id

        @app.put(route + '/<id>')
        @self.logger.request_log('Изменение документа')
        def put(id):
            return 'PUT ' + id

        @app.put(route + '/link/<id>')
        @self.logger.request_log('Изменение связи документа')
        @required_payload('type', 'link_id')
        def link(payload, id):
            return self.controller.create_document_link((int(id), *payload))

        @app.post(route)
        @self.logger.request_log('Добавление документа')
        @required_payload('content', 'header', 'type')
        def post(payload):
            return self.controller.create_document((payload))
