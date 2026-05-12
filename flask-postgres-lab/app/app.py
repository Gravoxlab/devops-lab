from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def home():

    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )

    conn.close()

    return "Connected to PostgreSQL!"

app.run(host='0.0.0.0', port=5000)
x
