import db_connector
from models.user import User

class UserRepository :

    def __init__(self) -> None:
        self.__connector = db_connector.get_db_connector()

    def create(self, name : str) :
        self.__connector.execute("INSERT INTO Users (name) VALUES (?)", [name])

    def get_user(self, id : int) :
        user = self.__connector.execute("SELECT * FROM Users WHERE id = ?", [id]).fetchone()
        return User(user[0], user[1])
    
    def get_all(self) :
        users = self.__connector.execute("SELECT * FROM Users").fetchall()
        output = []
        for u in users : output.append(User(u[0], u[1]))
        return output

    def delete_user(self, id : int) :
        self.__connector.execute("DELETE FROM Users WHERE id = ?", [id])

    def delete_all(self) :
        self.__connector.execute("DELETE FROM Users")
    