# syntax=docker/dockerfile:1
FROM python:3.7
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python -m pip install PyMySQL
RUN pip install PyMySQL
RUN pip install pymysql
RUN pip install --upgrade pip && \
    pip install pymysql
RUN docker-php-ext-install mysqli
RUN python3 -m pip install PyMySQL
RUN apk add --no-cache gcc musl-dev linux-headers

EXPOSE 5000
COPY src/
CMD ["python", "./app.py"]