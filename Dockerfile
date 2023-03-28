FROM python:3.11.2-slim

WORKDIR /usr/src/app

RUN pip install --no-cache-dir pyuwsgi

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER nobody
CMD ["uwsgi", "--http", ":8080", "--master", "-w", "app:app"]
