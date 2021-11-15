from initialize_db import initialize_database

def pytest_configure() :
    initialize_database()