import db_connector


def initialize_database():
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
        (id INTEGER PRIMARY KEY, description TEXT, amount INTEGER,
        user_id INTEGER, vat INTEGER)
        """)
    connector.execute(
        """
        CREATE TABLE Expenses
        (id INTEGER PRIMARY KEY, description TEXT,
        amount INTEGER, user_id, INTEGER, vat INTEGER)
        """)


if __name__ == '__main__':
    initialize_database()
