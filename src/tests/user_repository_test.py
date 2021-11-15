import unittest
from repositories.user_repository import UserRepository

class TestUserRepository(unittest.TestCase) :
    def setUp(self) -> None:
        self._user_repository = UserRepository()
        self._user_repository.delete_all()
    
    def test_create_user(self) :
        self._user_repository.create("Ada")
        users = self._user_repository.get_all()
        ada = users[0]

        self.assertEqual(len(users), 1)
        self.assertEqual(ada.name, "Ada")
        self.assertEqual(ada.id, 1)
    
    def test_get_user(self) :
        self._add_tree_users()
        user = self._user_repository.get_user(2)

        self.assertEqual(user.name, "Doe")
    
    def test_get_all(self) :
        self._add_tree_users()
        users = self._user_repository.get_all()

        self.assertEqual(len(users), 3)
    
    def test_delete_user(self) :
        self._add_tree_users()
        self._user_repository.delete_user(2)
        users = self._user_repository.get_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].name, "Ada")
        self.assertEqual(users[1].name, "John")
    
    def test_delete_all(self) :
        self._add_tree_users()
        self._user_repository.delete_all()
        users =self._user_repository.get_all()

        self.assertEqual(len(users), 0)
    
    def _add_tree_users(self) :
        self._user_repository.create("Ada")
        self._user_repository.create("Doe")
        self._user_repository.create("John")