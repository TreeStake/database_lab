import mysql.connector
from flask import Flask
from app.config import Config
from app.root import register_routes
import os
import sys
from app.database import db
from dotenv import load_dotenv
from flasgger import Swagger

print(sys.path)

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    register_routes(app)

    swagger = Swagger(app)

    create_database()
    create_tables(app)
    populate_data()
    return app


def create_database():
    connection = mysql.connector.connect(
        host=f'{DB_HOST}',
        user=f'{DB_USER}',
        password=f'{DB_PASS}',
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS kinderdb")
    cursor.close()
    connection.close()


def create_tables(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

def populate_data():
    sql_file_path = os.path.abspath('data.sql')
    if os.path.exists('data.sql'):
        connection = mysql.connector.connect(
            host=f'{DB_HOST}',
            user=f'{DB_USER}',
            password=f'{DB_PASS}',
            database=f'{DB_NAME}'
        )
        cursor = connection.cursor()
        with open(sql_file_path, 'r') as sql_file:
            sql_text = sql_file.read()
            sql_statements = sql_text.split(';')
            for statement in sql_statements:

                statement = statement.strip()
                if statement:
                    try:
                        cursor.execute(statement)
                        connection.commit()
                    except mysql.connector.Error as error:
                        print(f"Error executing SQL statement: {error}")
                        connection.rollback()
        cursor.close()
        connection.close()
