import mysql.connector
import sys
import bcrypt

class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Musharraf@123",
                database="hit_db_demo"
            )
            self.mycursor = self.conn.cursor()
        except Exception as e:
            print("Error:", e)
            sys.exit(0)
        else:
            print("Connected to Database")

    def register(self, name, email, password):
        try:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            self.mycursor.execute("""
                INSERT INTO users (name, email, password)
                VALUES (%s, %s, %s)
            """, (name, email, hashed_password))

            self.conn.commit()
        except Exception as e:
            print("Error:", e)
            return -1
        else:
            return 1