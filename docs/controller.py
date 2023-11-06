from docs.enums import Types
from tools.database import Database


def parse_document_data(data):
    return {
        'content': data[0],
        'header': data[1],
        'type': Types(data[2]).get_name(),
        'id': data[3]
    }


class DocumentController:
    def __init__(self, db: Database):
        self.db = db

    def create_document(self):
        return self.db.execute("""insert into docs (content, header, type, id) values (%s, %s, %s, %s);""", ('123', '123', 1, 1), fetch=False)

    def get_document(self, id):
        data = self.db.execute("""select * from public.docs where id = %s;""", (id), fetch=True)
        return parse_document_data(data)

    def get_all_documents(self):
        data = self.db.execute("""select * from public.docs;""", fetch=True)
        return [parse_document_data(row) for row in data]
