import db_connector
from models.user import User


class UserRepository:
    """Class responsible of interacting with Users-table (SQL database)
    """

    def __init__(self) -> None:
        """Constructor, database connector is called from db_connector.py-file
        """
        self.__connector = db_connector.get_db_connector()

    def create(self, name: str):
        """Creates new User to Users-table

        Args:
            name (str): Name of the user
        """
        self.__connector.execute("INSERT INTO Users (name) VALUES (?)", [name])

    def get_user(self, user_id: int)-> User:
        """Gets user row from Users-table and returns User-object

        Args:
            user_id (int): Id of user

        Returns:
            [type]: User-object
        """
        user = self.__connector.execute(
            "SELECT * FROM Users WHERE id = ?", [user_id]).fetchone()
        return User(user[0], user[1])

    def get_all(self):
        """Returns all users from Users-table as list of User-objects
        """
        users = self.__connector.execute("SELECT * FROM Users").fetchall()
        output = []
        for user in users:
            output.append(User(user[0], user[1]))
        return output

    def delete_user(self, user_id: int):
        """Deletes single user from Users-table

        Args:
            user_id (int): Id of user
        """
        self.__connector.execute("DELETE FROM Users WHERE id = ?", [user_id])

    def delete_all(self):
        """Deletes all users from Users-table
        """
        self.__connector.execute("DELETE FROM Users")
