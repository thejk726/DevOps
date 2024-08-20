# app/main.py
from flask import Flask, jsonify
import os
import psycopg2
import redis

app = Flask(__name__)

# PostgreSQL connection
def get_postgres_connection():
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host='db',
        port='5432'
    )
    return conn

# Redis connection
def get_redis_connection():
    r = redis.StrictRedis(host='redis', port=6379, decode_responses=True)
    return r

@app.route('/')
def index():
    return jsonify({"message": "Welcome to Flask with PostgreSQL and Redis!"})

@app.route('/db')
def db_test():
    conn = get_postgres_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT version();')
    db_version = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify({"PostgreSQL version": db_version})

@app.route('/redis')
def redis_test():
    r = get_redis_connection()
    r.set('test', 'Hello, Redis!')
    value = r.get('test')
    return jsonify({"Redis value": value})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
