from flask import Flask
app = Flask(__name__)

from utils.utils import dataSource


@app.route('/')
def home():
    return '<h1>Hello World</h2>'

@app.route('/json')
def data():
    return dataSource()

if __name__ == "__main__":
    app.run(debug=True)

