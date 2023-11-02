from flask import Flask
from flask_restful import Api

from docs.api import DocumentApi

app = Flask(__name__)

api = Api()
DocumentApi(app, '/document')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='localhost', port=8081, threaded=True)
