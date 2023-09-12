# ベースイメージを選択
FROM python:3.8

# パッケージのアップデート
RUN apt-get update

# アプリケーションファイルをコピー
COPY . /app

# ワーキングディレクトリを設定
WORKDIR /app

# アプリケーションの依存関係をインストール
RUN pip install -r requirements.txt

# アプリケーションを実行
# CMD ["exec","python", "main.py"]
CMD ["bash"]
