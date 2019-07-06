
import os
import psycopg2

from schema import database_tables

tables = database_tables()

dev_db_url = os.getenv('DATABASE_URI')
test_db_url = os.getenv('TEST_DATABASE_URI')

# create connection to db
def connection(url):
    conn = psycopg2.connect(url, dns=None)
    return conn

# create tables
def init_db():
    conn = connection(dev_db_url)
    cur = conn.cursor()

    for table in tables:
        cur.execute(table)
    conn.commit()
    return conn

# create test tables
def init_testdb():
    conn = connection(test_db_url)
    cur = conn.cursor()

    for table in tables:
        cur.execute(table)
    conn.commit()
    return conn

# drop all tables    
def drop_all():
    conn = connection(test_db_url)
    cur = conn.cursor()
    
    query = """DROP TABLE if exists comments, meetups, questions, rsvps, users;"""
    cur.execute(query)
    conn.commit()

