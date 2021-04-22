from flask import Flask, render_template, request, session, url_for, redirect
from flask.views import MethodView
import random

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html", title="Index", message='※Vue.js',
                           data="['one', 'two', 'three']")


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
