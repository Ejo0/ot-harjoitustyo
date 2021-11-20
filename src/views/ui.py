from views.home_view import HomeView
from views.user_view import UserView
from tkinter import *
from models.user import User

class UI :

    def __init__(self, parent) -> None:
        self._parent = parent
        self._view = None

    def start(self) :
        self.show_home_view()
    
    def show_home_view(self) :
        self._hide_current_view()
        self._view = HomeView(self._parent, self.show_user_view)
        self._view.start()
    
    def show_user_view(self, user : User) :
        self._hide_current_view()
        self._view = UserView(self._parent, user, self.show_home_view)
        self._view.start()
    
    def _hide_current_view(self) :
        if self._view : self._view.destroy()
        self._view = None