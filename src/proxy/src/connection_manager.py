import os
import psycopg2
from psycopg2 import pool

class ConnectionManager:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.pool = psycopg2.pool.ThreadedConnectionPool(
                minconn=int(os.getenv("PG_MIN_CONN", 5)),
                maxconn=int(os.getenv("PG_MAX_CONN", 20)),
                host=os.getenv("PG_HOST"),
                database=os.getenv("PG_DB"),
                user=os.getenv("PG_USER"),
                password=os.getenv("PG_PASSWORD")
            )
        return cls._instance
    
    def get_conn(self):
        return self.pool.getconn()
    
    def put_conn(self, conn):
        self.pool.putconn(conn)
    
    def close_all(self):
        self.pool.closeall()
