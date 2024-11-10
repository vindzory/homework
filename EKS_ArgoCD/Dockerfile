
FROM python:3.9-slim

RUN apt-get update && apt-get install -y libmysqlclient-dev
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=appdb
FROM mysql:8.0
COPY ./init.sql /docker-entrypoint-initdb.d/

EXPOSE 5000 3306

CMD ["python", "app.py"]