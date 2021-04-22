# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for
from collections import OrderedDict

import numpy as np
import pandas as pd

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

# ここからウェブアプリケーション用のルーティングを記述
# index にアクセスしたときの処理
@app.route('/')
def index():
    title = "ようこそ"
    df = pd.read_csv(filepath_or_buffer="data.csv", encoding="utf8", sep=",", dtype=str, skiprows=1, names=["dir", "fileid", "color", "item"])
    df.insert(4, "image", df["dir"] + '/' + df["fileid"] + '/' + df["fileid"] + '-1')
    data = df.to_dict("records", into=OrderedDict)

    # index.html をレンダリングする
    return render_template('index.html', title=title, data=data)

if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に