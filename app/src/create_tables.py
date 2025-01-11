import sys
import sqlite3 as sq

sql_creation_tables = (
    """CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
tg_id INTEGER,
profile_id INTEGER   
)""",

    """CREATE TABLE IF NOT EXISTS profile (
id INTEGER PRIMARY KEY,
users_id INTEGER
) """,

    """CREATE TABLE IF NOT EXISTS timer (
id INTEGER PRIMARY KEY,
users_id INTEGER,
begin_time datetime,
stop_time datetime
)  """

)

def create_tables():
    with sq.connect(sys.path[0]+'\\db.sqlite3') as connection:
        cursor = connection.cursor()
        for sql in sql_creation_tables:
            cursor.execute(sql)

if __name__=='__main__':
    create_tables()