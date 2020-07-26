from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('timeweb.config.Config')
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = 'parsers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(512), nullable=False)
    res = db.Column(db.String, nullable=True, default=None)

    def __init__(self, url, res=None):
        self.url = url
        self.res = res


@app.route('/')
def hello_world():
    return jsonify(post="/api/v1", get='/api/v1/get?id=x')


@app.route('/api/v1', methods=['POST'])
def post():
    data = Data(request.form.get('url'))
    db.session.add(data)
    db.session.commit()

    return jsonify(id=data.id)


@app.route('/api/v1/get')
def get():
    req = request.args.get('id')
    test = Data.query.filter_by(id=req).first()
    print(test.url)

    return jsonify(data=test.url, val=test.res)


def crawler(url):
    request.get(url)