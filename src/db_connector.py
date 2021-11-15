import sqlite3
import os
from dotenv import load_dotenv

directory = os.path.dirname(__file__)
load_dotenv(dotenv_path=os.path.join(directory, '..', '.env.prod'))

db_name = os.getenv('DATABASE_NAME')
db_path = os.path.join(directory, '..', 'data', db_name)

db_connector = sqlite3.connect(db_path)
db_connector.isolation_level = None

def get_db_connector():
    return db_connector