from unittest import TestCase
from services.user_service import UserService
from repositories.user_repository import UserRepository


class TestUserService(TestCase):


    def setUp(self) -> None:
        self._user_service = UserService()
        self._user_repository = UserRepository()
        self._user_repository.delete_all()
        self._user_service.create('Doe')
        self._user_service.create('Ada')
        self._user_service.create('Foo')
    
    def test_get_user_gives_correct_one(self):
        user = self._user_service.get_user(2)
        self.assertEqual(user.name, 'Ada')
    
    def test_get_all_users_lenght_matches(self):
        users = self._user_service.get_all()
        self.assertEqual(len(users), 3)