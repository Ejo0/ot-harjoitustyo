from tkinter import *
from services.user_service import UserService


INFOTEXT = """SimpleAccountingTool-kirjanpitosovellus

Sovelluksen avulla voi pitää kirjaa toiminimen myynti- ja ostotapahtumista. Sovellus tarjoaa listauksen kirjatuista tapahtumista yhdenkertaisen
kirjanpidon periaatteella. Lisäksi sovellus näyttää yhteenvedon kassavirrasta, tuloslaskelmasta sekä alv-kertymästä. Sovellukseen voi luoda useita käyttäjiä.

KÄYTTÖOHJEET:

1. Kotivalikko
Sovelluksen käynnistys avaa kotivalikon, jossa on kaksi osiota: Info-osio sisältää sovelluksen käyttöohjeet.
Käyttäjät-osiosta pääsee luomaan uuden käyttäjän ja kirjautumaan olemassa olevana käyttäjänä.

2. Käyttäjän luominen ja valitseminen.
Uuden käyttäjän saa luotua Käyttäjät-näkymästä lisäämällä halutun nimen ja klikkaamalla 'Luo käyttäjä'.
Luodut käyttäjät listataan alla sinisissä palkeissa. Palkkia klikkaamalla voi kirjautua kyseisen käyttäjän näkymään.

3. Tapahtuman lisääminen
Navigoi Käyttäjä-näkymässä kohtaan 'Lisää tapahtuma'. Täytä vaaditut kentät seuraavasti:
- Valitse tyypiksi Myynti tai Osto
- Merkitse tapahtuman päivämäärä (esim. 1.1.2000)
- Merkitse summa (euroina), joka sisältää mahdollisen arvonlisäveron. Hyväksyttyjä syötteitä esim. '10', '10,5', '10.05'
- Valitse tapahtuman mukainen alv-kanta (24, 14, 10 tai 0 prosenttia)
- Lisää kuvaus (pituus 1-50 merkkiä)
Kun tiedot on syötetty, tapahtuman saa lisättyä klikkaamalla 'Luo tapahtuma'. Sovellus vahvistaa onnistuneen tapahtuman lisäämisen.

4. Tapahtuman korjaaminen
Lisättyä tapahtumaa ei voi muokata tai poistaa. Virheellisen tapahtuman voi oikaista lisäämällä vastaava tapahtuma uudestaan,
mutta summa –merkkisenä. Näin tapahtumat kumoavat toisensa ja yhteisvaikutus on +/- 0.

5. Kooste
Käyttäjät-näkymän Kooste-osio näyttää kirjanpidon tapahtumista aikajärjestyksessä, myynnit ja ostot eroteltuna.
Lisäksi näkymästä löytyy seuraavat tunnusluvut:
- Kassavirta kertoo myynneistä kassaan (tilille) kertyneet rahat sekä ostoihin käytetyt rahat, sisältäen mahdolliset alvit.
- Tuloslaskelma näyttää myyntien ja ostojen summat (ilman alvia) sekä näiden erotuksen, eli tuloksen.
- Alv-laskelma näyttää myyntien sekä ostojen alvien summat sekä näiden erotuksen. Erotus kertoo verottajalle maksettavaksi jäävän alvin summan.

Kooste-osiossa tapahtumia voi hakea myös aikavälillä valitsemalla alku- ja/tai loppupäivämäärän muodossa 1.1.2000. Klikkaamalla 'Hae', Kooste-
osio päivittyy ja näyttää sekä tapahtumat että tunnusluvut valitun aikavälin mukaisesti.
Käyttäjä-näkymästä pääsee takaisin kotivalikkoon klikkaamalla punaista 'Poistu'-painiketta.
"""


class HomeView:

    def __init__(self, parent, show_user_view) -> None:
        self._parent = parent
        self._show_user_view = show_user_view
        self._header = None
        self._body = None
    
    def start(self):
        self._header = Header(self._parent, self._show_info, self._show_users)
        self._header.pack()
        self._show_users()
    
    def _show_info(self):
        self._hide_body()
        self._body = InfoMenu(self._parent)
        self._body.pack()
    
    def _show_users(self):
        self._hide_body()
        self._body = UsersMenu(self._parent, self._show_user_view, self._show_users)
        self._body.pack()

    def _hide_body(self):
        if self._body : self._body.destroy()
        self._body = None

    def destroy(self):
        if self._header : self._header.destroy()
        if self._body : self._body.destroy()
        self._header = None
        self._body = None

class Header:

    def __init__(self, parent, show_info, show_user) -> None:
        self._parent = parent
        self._show_info = show_info
        self._show_user = show_user
        self._frame = None

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill='both')
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = Frame(
            master=self._parent,
            bg='white',
        )
        users_menu_button = Button(
            master=self._frame,
            text="Käyttäjät", 
            relief='flat',
            command=lambda: self._show_user(),
            bg='white',
            highlightthickness=0,
            activeforeground='white',
            activebackground='black',
            font=('monospace', 16, 'bold')
        )
        info_menu_button = Button(
            master=self._frame,
            text='Info',
            relief='flat',
            command=lambda: self._show_info(),
            bg='white',
            highlightthickness=0,
            activeforeground='white',
            activebackground='black',
            font=('monospace', 16, 'bold')
        )
        users_menu_button.grid(padx=80, pady=5)
        info_menu_button.grid(row=0, column=1, padx=80, pady=5)

class InfoMenu:

    def __init__(self, parent) -> None:
        self._parent = parent
        self._frame = None

        self._initialize_()
    
    def pack(self):
        self._frame.pack(fill='both', expand=1)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize_(self):
        self._frame = Frame(master=self._parent, bg='white')
        info_text = Text(master=self._frame, relief='flat')
        info_text.insert(END, INFOTEXT)
        info_text.pack(fill='both',expand=1, padx=5, pady=5)
        info_text.config(state=DISABLED)

class UsersMenu:

    def __init__(self, parent, show_user_view, show_users) -> None:
        self._parent = parent
        self._show_user_view = show_user_view
        self._show_users = show_users
        self._frame = None
        self._user_service = UserService()
    
        self._initialize()
    
    def pack(self):
        self._frame.pack(fill='both', expand=True)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = Frame(master=self._parent, bg='white')
        users_label = Label(
            master=self._frame,
            text="Luo uusi käyttäjä",
            bg='white'
        )
        new_user_label = Label(
            master=self._frame,
            text='Nimi',
            bg='white'
        )
        new_user_entry = Entry(
            master=self._frame,
        )
        new_user_button = Button(
            master=self._frame,
            text='Luo käyttäjä',
            command=lambda: self._create_user(new_user_entry.get()),
            bg='white',
            highlightthickness=0,
            activeforeground='white',
            activebackground='black',
        )
        pick_users_label = Label(
            master=self._frame,
            text='Valitse käyttäjä',
            bg='white'
        )
        users_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        new_user_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
        new_user_entry.grid(row=1, column=1, padx=5, pady=5)
        new_user_button.grid(row=1, column=2, padx=5, pady=5, sticky='w')
        pick_users_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')

        new_user_entry.focus()

        self._frame.grid_rowconfigure(2, minsize=30)
        for i in range(6):
            self._frame.grid_columnconfigure(i, minsize=200)

        col_index = 0
        for user in self._user_service.get_all():
            user_button = Button(
                master=self._frame,
                text=f"{user.name}",
                command=lambda u=user: self._show_user_view(u),
                bg = 'deepskyblue',
                width=20,
                anchor='nw'
            )
            user_button.grid(row=4 + col_index//6, column=col_index%6, columnspan=2, padx=5, pady=15, sticky='w')
            col_index += 2

    def _create_user(self, name):
        if len(name) == 0 : return 
        self._user_service.create(name)
        self._show_users()
        