import psycopg2

HOST = "192.168.56.100"
DBNAME = "br_project"
USERNAME = "postgres"
PASSWORD = "postgre"
CONNECTION = psycopg2.connect(host=HOST, dbname=DBNAME, user=USERNAME, password=PASSWORD)


class PlayerInfoInsert:
    pass