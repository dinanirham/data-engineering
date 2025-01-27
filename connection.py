import os
import json
import psycopg2
import pyodbc
from sqlalchemy import create_engine
import time

def time_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Elapsed time: {(end - start) * 1000:.3f}ms")
        return res
    return wrapper


def config(connection_db):
    full_path = 'config.json'
    with open(full_path) as file:
        conf =json.load(file)[connection_db]
    return conf

@time_func
def postgres(conf, name_conn):
    try:
        conn_ = psycopg2.connect(
               host=conf['host'],
               database=conf['db_name'],
               user=conf['user'],
               password=conf['password'],
               port=conf['port']
        )
        engine_ = create_engine(f"postgresql+psycopg2://{conf['user']}:{conf['password']}@{conf['host']}:{conf['port']}/{conf['db_name']}")
        print(f'[INFO] Connection to PostgreSQL {name_conn} is successful')
        return conn_, engine_

    except Exception as e:
        print(f"[INFO] Connection to PostgreSQL {name_conn} is failed")
        print(str(e))

@time_func        
def sqlserver(conf, name_conn):
    try:
        conn_ = pyodbc.connect(f"DRIVER={conf['driver']};\
                                SERVER={conf['host']};\
                                DATABASE={conf['db_name']};\
                                UID={conf['user']};\
                                PWD={conf['password']}"
                             )
        print(f'[INFO] Connection to SQL Server {name_conn} is successful')
        return conn_
    
    except Exception as e:
        print(f"[INFO] Connection to SQL Server {name_conn} is failed")
        print(str(e))