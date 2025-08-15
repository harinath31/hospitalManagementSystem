import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nisanth@123", # Add your MySQL password
        database="hospital_db"
    )

