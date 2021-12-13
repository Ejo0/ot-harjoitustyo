import db_connector


def initialize_database():
    """Initializes database -> removes tables if they exist, and then creates
    tables Users, Sales and Expenses. Uses database connector -object from db_connector.py
    """
    connector = db_connector.get_db_connector()

    connector.execute("DROP TABLE IF EXISTS Users")
    connector.execute("DROP TABLE IF EXISTS Sales")
    connector.execute("DROP TABLE IF EXISTS Expenses")

    connector.execute(
        """
        CREATE TABLE Users
        (id INTEGER PRIMARY KEY, name TEXT)
        """)
    connector.execute(
        """
        CREATE TABLE Sales
        (id INTEGER PRIMARY KEY, user_id INTEGER, event_date DATE,
        amount INTEGER, vat INTEGER, description TEXT)
        """)
    connector.execute(
        """
        CREATE TABLE Expenses
        (id INTEGER PRIMARY KEY, user_id INTEGER, event_date DATE,
        amount INTEGER, vat INTEGER, description TEXT)
        """)


if __name__ == '__main__':
    initialize_database()
