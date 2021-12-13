import sqlite3
import os
from dotenv import load_dotenv

"""
Database file(s) are located in: ot-harjoitustyo/data/
Environment variables (table names) are determined in .env.prod and .env.test -files
The production environment is .env.prod, and path is given to load_dotenv.
Test environment is determined in pytest.ini -> env.test. This is done before load_dotenv-function,
which won't override already determined environment-variable.

Depending on environment, database name will be 'prod_database.db' or 'test_database.db'
and the path to correct file is given to db_connector, which can be called using
get_db_connector-function.
"""

directory = os.path.dirname(__file__)
load_dotenv(dotenv_path=os.path.join(directory, '..', '.env.prod'))

db_name = os.getenv('DATABASE_NAME')
db_path = os.path.join(directory, '..', 'data', db_name)

db_connector = sqlite3.connect(db_path)
db_connector.isolation_level = None


def get_db_connector():
    """Returns db_connector object
    """
    return db_connector
