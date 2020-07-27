from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__)
app.config['DEBUG'] = False
app.config.from_object('timeweb.config.Config')
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = 'parsers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String, nullable=False)
    res = db.Column(db.Text, nullable=True, default=None)

    def __init__(self, url, res=None):
        self.url = url
        self.res = res


@app.route('/')
def hello_world():
    return jsonify(post="/api/v1", get='/api/v1/get?id={1}')


@app.route('/api/v1', methods=['POST'])
def post():
    if request.form.get('url') is None:
        abort(400, 'url is empty')

    data = Data(request.form.get('url'))
    db.session.add(data)
    db.session.commit()

    return jsonify(id=data.id)


@app.route('/api/v1/')
def get():
    req = request.args.get('id')
    fin = Data.query.filter_by(id=req).first()
    parse = crawler(fin.url)
    fin.res = parse
    db.session.commit()

    return jsonify(url=fin.url, html=fin.res)


def crawler(url):
    try:
        if 'http' not in url:
            url = 'http://' + url
        data = requests.get(url)

        return data.content

    except requests.exceptions.RequestException:
        return abort(403, 'given url not responding')


