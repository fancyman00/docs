from docs.enums import Types
from tools.database import Database


def parse_document_data(data):
    return {
        'content': data[0],
        'header': data[1],
        'type': Types(data[2]).get_name(),
        'id': data[3]
    }


CREATE_DOCUMENT_QUERY = """insert into docs (content, header, type, id) values (%s, %s, %s, nextval('unique_id'));"""
GET_DOCUMENT_QUERY = """select * from public.docs where id = %s;"""
GET_ALL_DOCUMENT_QUERY = """select * from public.docs;"""


class DocumentController:
    def __init__(self, db: Database):
        self.db = db

    def create_document(self, args_tuple: tuple):
        return self.db.execute(CREATE_DOCUMENT_QUERY, args=args_tuple, fetch=False)

    def get_document(self, id: int):
        data = self.db.execute(GET_DOCUMENT_QUERY, args=(id), fetch=True)
        return parse_document_data(data)

    def get_all_documents(self, count):
        data = self.db.execute(GET_ALL_DOCUMENT_QUERY, fetch=True, count=count)
        if isinstance(data, list):
            return [parse_document_data(row) for row in data]
        else:
            return [parse_document_data(row) for row in [data]]
