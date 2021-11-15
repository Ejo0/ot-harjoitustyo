from tkinter import *
from repositories.user_repository import UserRepository

class HomeView :

    def __init__(self, parent) -> None:
        self._parent = parent
        self._header = None
        self._body = None
    
    def start(self) :
        self._header = Header(self._parent, self._show_info, self._show_users)
        self._header.pack()
        self._show_info()
    
    def _show_info(self) :
        self._hide_body()
        self._body = InfoMenu(self._parent)
        self._body.pack()
    
    def _show_users(self) :
        self._hide_body()
        self._body = UsersMenu(self._parent)
        self._body.pack()

    def _hide_body(self) :
        if self._body : self._body.destroy()
        self._body = None


class Header :

    def __init__(self, parent, show_info, show_user) -> None:
        self._parent = parent
        self._show_info = show_info
        self._show_user = show_user
        self._frame = None

        self._initialize()
    
    def pack(self) :
        self._frame.pack(fill='both')
    
    def _initialize(self) :
        self._frame = Frame(master=self._parent, bg='white')
        users_menu_button = Button(
            master=self._frame,
            text="Käyttäjät", 
            relief='flat',
            command=self._show_user,
            bg='white',
            highlightthickness=0,
            activeforeground='white',
            activebackground='black',
        )
        info_menu_button = Button(
            master=self._frame,
            text='Info',
            relief='flat',
            command= self._show_info,
            bg='white',
            highlightthickness=0,
            activeforeground='white',
            activebackground='black'
        )
        users_menu_button.grid(padx=20, pady=5)
        info_menu_button.grid(row=0, column=1, padx=20, pady=5)

class InfoMenu :

    def __init__(self, parent) -> None:
        self._parent = parent
        self._frame = None

        self._initialize_()
    
    def pack(self) :
        self._frame.pack()
    
    def destroy(self) :
        self._frame.destroy()
    
    def _initialize_(self) :
        self._frame = Frame(master=self._parent)
        info_text = Text(master=self._frame)
        info_text.insert(END, "Placeholder infotekstille\nuseampi rivi")
        info_text.pack()

class UsersMenu :

    def __init__(self, parent) -> None:
        self._parent = parent
        self._frame = None
        self._user_repository = UserRepository()
    
        self._initialize()
    
    def pack(self) :
        self._frame.pack(fill='both', expand=True)
    
    def destroy(self) :
        self._frame.destroy()
    
    def _initialize(self) :
        self._frame = Frame(master=self._parent)
        users_label = Label(
            master=self._frame,
            text="Valitse käyttäjä tai luo uusi",
            bg='white'
        )
        new_user_button = Button(
            master=self._frame,
            text='Luo käyttäjä',
            relief='flat',
            command=lambda: self._create_user(),
            bg='white',
            highlightthickness=0,
            activeforeground='white',
            activebackground='black'
        )
        self._frame.grid_rowconfigure(1, minsize=30)
        users_label.grid(row=0, column=0)
        new_user_button.grid(row=2, column=0, sticky='w')

        for u in self._user_repository.get_all() :
            user_button = Button(self._frame, text=(u.name))
            user_button.grid()

    def _create_user(self) :
        self._user_repository.create("Ada")
        user = Button(self._frame, text=("Ada"))
        user.grid()