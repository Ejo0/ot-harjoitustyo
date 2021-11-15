from views.home_view import HomeView
from tkinter import *

class UI :

    def __init__(self, parent) -> None:
        self._parent = parent
        self._view = None

    def start(self) :
        self._show_home_view()
    
    def _show_home_view(self) :
        self._view = HomeView(self._parent)
        self._view.start()