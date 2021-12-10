from repositories.user_repository import UserRepository


class UserService:
    """Interface for GUI to create Users and get info from Users database
    """


    def __init__(self) -> None:
        """Constructor, UserRepository is initialized
        """
        self._user_repository = UserRepository()

    def create(self, name: str):
        """Adds new User to database

        Args:
            name (str): Name of user
        """
        self._user_repository.create(name)

    def get_user(self, user_id: int):
        """Gets user from database using individual ID of User

        Args:
            user_id (int): User ID

        Returns:
            User: User-object
        """
        return self._user_repository.get_user(user_id)

    def get_all(self)-> list:
        """Returns all Users from database

        Returns:
            list: A list containing User-objects
        """
        users = self._user_repository.get_all()
        return users
