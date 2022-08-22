# -*- coding:utf-8 -*-
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world"


@app.route("/<string:name>")
def hello_name(name):
    return f"hello world {name}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)


