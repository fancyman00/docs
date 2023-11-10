from docs.enums import Types
from tools.database import Database


def parse_document_data(data):
    return {
        'id': data[0],
        'content': data[1],
        'header': data[2],
        'type': Types(data[3]).get_name(),
        'linkId_type': data[4]
    }


CREATE_DOCUMENT_QUERY = """insert into public.docs (content, header, type, id) values (%s, %s, %s);"""
CREATE_DOCUMENT_LINK_QUERY = """insert into doc_links (id, type, link_id) values (%s, %s, %s);"""
GET_DOCUMENT_QUERY = """SELECT docs.id, docs.content, docs.header, docs.type,
       array_agg(array[doc_links.link_id, doc_links.type]) as links
FROM docs left join doc_links ON docs.id=doc_links.id where docs.id = %s GROUP BY docs.id, docs.content, docs.header, docs.type
ORDER BY docs.id;"""
GET_ALL_DOCUMENT_QUERY = """SELECT docs.id, docs.content, docs.header, docs.type,
       array_agg(array[doc_links.link_id, doc_links.type]) as links
FROM docs left join doc_links ON docs.id=doc_links.id GROUP BY docs.id, docs.content, docs.header, docs.type
ORDER BY docs.id;"""


class DocumentController:
    def __init__(self, db: Database):
        self.db = db

    def create_document(self, args_tuple: tuple):
        return self.db.execute(CREATE_DOCUMENT_QUERY, args=args_tuple)

    def get_document(self, id: int):
        data = self.db.execute(GET_DOCUMENT_QUERY, args=(id), fetch=True)[0]
        return parse_document_data(data)

    def get_all_documents(self, count):
        data = self.db.execute(GET_ALL_DOCUMENT_QUERY, fetch=True, count=count)
        if isinstance(data, list):
            return [parse_document_data(row) for row in data]
        else:
            return [parse_document_data(row) for row in [data]]

    def edit_document(self, id):
        return 'PUT'

    def create_document_link(self, args_tuple):
        return self.db.execute(CREATE_DOCUMENT_LINK_QUERY, args=args_tuple)