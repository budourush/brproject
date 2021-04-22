# pythonの3.7.2-slimをベースにする
FROM python:3.7.2-slim

# ARGで変数を定義
# buildする時に変更可能
# コンテナ内のディレクトを決めておく
ARG root_directory=/lalapp

# python3 pipのインストール
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    # imageのサイズを小さくするためにキャッシュ削除
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    # pipのアップデート
    && pip install --upgrade pip

# Dockerfileを実行したディレクトにあるファイルを全てイメージにコピー
COPY . ${root_directory}/

# 機械学習に使用するライブラリのインストール
WORKDIR ${root_directory}/pip/

RUN pip install -r requirements.txt

# ディレレクトリの移動
WORKDIR ${root_directory}
