from flask import Flask
from docs.api import DocumentApi
from tools.database import Database

app = Flask(__name__)
database = Database('postgres', '123', '127.0.0.1', '5432')

DocumentApi(app, '/document', database)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='localhost', port=8081, threaded=True)
