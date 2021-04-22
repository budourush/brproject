# recommendApp

LowcalによるAIのPoCプロジェクト

## 環境構築手順

### 1. dockerのインストール

docker for windows か docker for mac
※インストールにはアカウント登録が必要

### 2. gitのインストール

git for windows とか

### 3. gitで本リポジトリをローカルに取得

`git clone https://github.com/lowcal-ai-labo/recommendApp.git`

### 4. git clone したフォルダで以下を実行

`docker-compose up -d`
※ここで環境を構築するので少し時間かかります

### 5. 作成したコンテナ内部へ

`docker exec -it lal_app /bin/sh -c "[ -e /bin/bash ] && /bin/bash || /bin/sh"`

### 6. flask起動(コンテナ内部で)

`python main.py`

### 7. ブラウザ確認

`http://localhost:5000`でアクセス
「hello」と表示されます。
