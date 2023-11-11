import json

from flask import request

from docs.controller import DocumentController
from tools.logger import Logger
from tools.request import required_payload, error


class DocumentApi:
    def __init__(self, app, route, db):
        self.logger = Logger(app)
        self.controller = DocumentController(db)

        @app.get(route + '/<id>')
        @error
        @self.logger.request('Получение документа')
        def get(id):
            body = self.controller.get_document(id)
            return json.dumps(body)

        @app.get(route)
        @error
        @self.logger.request('Получение документов')
        def get_all():
            count = request.args.get('count')
            body = self.controller.get_all_documents(count)
            return json.dumps(body)

        @app.delete(route + '/<id>')
        @error
        @self.logger.request('Удаление документа')
        def delete(id):
            return self.controller.delete_document(id)

        @app.put(route + '/<id>')
        @error
        @self.logger.request('Изменение документа')
        def put(id):
            return 'PUT ' + id

        @app.post(route + '/link/<id>')
        @error
        @self.logger.request('Изменение связи документа')
        @required_payload('type', 'link_id')
        def link(payload, id):
            return self.controller.create_document_link((int(id), *payload))

        @app.delete(route + '/link/<id>')
        @error
        @self.logger.request('Удаление связи документа')
        @required_payload('type', 'link_id')
        def delete_link(payload, id):
            return self.controller.delete_document_link((int(id), *payload))

        @app.post(route)
        @error
        @self.logger.request('Добавление документа')
        @required_payload('content', 'header', 'type')
        def post(payload):
            return self.controller.create_document((payload))
