FROM python:3.10.8

WORKDIR /usr/src/app

RUN pip install --no-cache-dir pyuwsgi

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER nobody
CMD ["uwsgi", "--http", ":8080", "--master", "-w", "app:app"]
