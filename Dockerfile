FROM python:3.7

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP flask_api.py
ENV FLASK_PORT 5000

EXPOSE $FLASK_PORT

ENV STRINGS ab,xyz,ab,abc,def
ENTRYPOINT flask run --host=0.0.0.0 --port=$FLASK_PORT