class User:
    """Represents one User of the application
    """

    def __init__(self, user_id: int, name: str) -> None:
        """Constructor, where name and user id are set

        Args:
            user_id (int): User ID, from Users-table
            name (str): Name of user
        """
        self.__id = user_id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
