import time

import redis
from flask import Flask

import pymysql

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def connection():
    s = 'db' #Your server(host) name 
    d = 'MyDataBase' 
    u = 'user' #Your login user
    p = 'test' #Your login password
    conn = pymysql.connect(host=s, user=u, password=p, database=d)
    return conn

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    # count = get_hit_count()
    # return 'Hello World!I Danil and i slave this lab. I have been seen {} times.\n'.format(count)
    users = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Person")

    for row in cursor.fetchall():
        # users.append({"id": row[0], "First_Name": row[1], "Last_Name": row[2]})
        users.append(f"{row[0]} - {row[1]} - {row[2]} <br>")
        print(row)
    conn.close()
    return '{}'.format("".join(users))