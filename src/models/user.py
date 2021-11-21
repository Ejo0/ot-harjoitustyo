class User:

    def __init__(self, user_id: int, name: str) -> None:
        self.__id = user_id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
