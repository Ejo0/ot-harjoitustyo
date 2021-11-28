from repositories.user_repository import UserRepository


class UserService:


    def __init__(self) -> None:
        self._user_repository = UserRepository()

    def create(self, name: str):
        self._user_repository.create(name)

    def get_user(self, user_id: int):
        return self._user_repository.get_user(user_id)

    def get_all(self):
        users = self._user_repository.get_all()
        return users
