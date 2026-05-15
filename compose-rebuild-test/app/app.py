from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("POSTGRES_HOST")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")


@app.route("/")
def home():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        connection.close()

        return "Flask Connected To Database"

    except Exception as e:
        return f"Database connection failed: {e}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
