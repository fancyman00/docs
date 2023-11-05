from tools.database import Database


class DocumentController:
    def __init__(self, db: Database):
        self.db = db

    def create_document(self):
        return self.db.execute("""insert into docs (content, header, type, id) values (%s, %s, %s, %s);""", ('123', '123', 1, 1), fetch=False)
