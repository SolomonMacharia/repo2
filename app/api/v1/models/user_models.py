
import time 

from manage import connection

conn = connection()
cur = conn.cursor()


class User:
    def __init__(self):
        self.registered_on = time.asctime(time.localtime(time.time()))

    def create_user(self, username, email, password, is_admin=False):
        query = """INSERT INTO users(username, email, password, is_admin, registered_on) VALUES(%s, %s, %s, %s, %s) RETURNING username, email, is_admin, registered_on;"""
        cur.execute(query, (username, email, password ))
        created_user = cur.fetchone()
        conn.commit()
        return created_user