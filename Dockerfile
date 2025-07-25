# 公式のPython 3.13ランタイムイメージを使用
FROM python:3.13

# 環境変数を設定
# Pythonがpycファイルをディスクに書き込むのを防ぐ
ENV PYTHONDONTWRITEBYTECODE=1
# Pythonの標準出力・エラー出力のバッファリングを無効化
ENV PYTHONUNBUFFERED=1 

# コンテナ内の作業ディレクトリを設定
WORKDIR /code

# requirements.txtをコピーして依存関係をインストール
COPY requirements.txt /code/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Djangoプロジェクト全体をコンテナにコピー
COPY . /code/

# Djangoポートを公開
EXPOSE 8000

# Gunicornで本番向けサーバーを起動
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "twitter_api.wsgi:application"]
