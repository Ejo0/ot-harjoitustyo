from tkinter import *
from repositories.sales_repository import SalesRepository
from models.user import User

class UserView:

    def __init__(self, parent, user : User, show_home_view) -> None:
        self._parent = parent
        self._user = user
        self._show_home_view = show_home_view
        self._sales_repository = SalesRepository()
        self._header = None
        self._body = None

    def start(self):
        self._header = Header(self._parent, self._user, self._show_new_event, self._show_statistics, self._show_home_view)
        self._header.pack()
        self._show_statistics()
    
    def destroy(self):
        self._hide_body()
        if self._header : self._header.destroy()
        self._header = None

    def _show_new_event(self):
        self._hide_body()
        self._body = NewEvent(self._parent, self._user, self._sales_repository)
        self._body.pack()
    
    def _show_statistics(self):
        self._hide_body()
        self._body = Statistics(self._parent, self._user, self._sales_repository)
        self._body.pack()
    
    def _hide_body(self):
        if self._body : self._body.destroy()
        self._body = None

    
class Header:

    def __init__(self, parent, user : User, show_new_event, show_statistics, show_home_view) -> None:
        self._parent = parent
        self._user = user
        self._show_new_event = show_new_event
        self._show_statistics = show_statistics
        self._show_home_view = show_home_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill='both')
    
    def destroy(self):
        if self._frame : self._frame.destroy()
        self._frame = None

    def _initialize(self):
        self._frame = Frame(master=self._parent, bg='white')
        header_label = Label(
            master=self._frame,
            text=f"Hei {self._user.name}!",
            bg='white',
            font=('monospace', 14, 'bold')
        )
        show_new_event_button = Button(
            master=self._frame,
            text="Lisää tapahtuma",
            relief='flat',
            command=self._show_new_event,
            bg='white',
            highlightthickness=0,
            activeforeground='white',
            activebackground='black',
            font=('monospace', 16, 'bold')
        )
        show_statistics_button = Button(
            master=self._frame,
            text="Kooste",
            relief='flat',
            command=self._show_statistics,
            bg='white',
            highlightthickness=0,
            activeforeground='white',
            activebackground='black',
            font=('monospace', 16, 'bold')
        )
        show_home_view_button = Button(
            master=self._frame,
            text="Poistu",
            relief='flat',
            command=self._show_home_view,
            bg='white',
            highlightthickness=0,
            activeforeground='white',
            activebackground='black',
            foreground='red',
            font=('monospace', 16, 'bold')
        )
        header_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        show_new_event_button.grid(row=1, column=0, padx=80, pady=5)
        show_statistics_button.grid(row=1, column=1, padx=80, pady=5)
        show_home_view_button.grid(row=1, column=2, padx=80, pady=5)


class NewEvent:

    def __init__(self, parent, user : User, sales_repository : SalesRepository) -> None:
        self._parent = parent
        self._user = user
        self._sales_repository = sales_repository
        self._frame = None
        self._notification_label = None

        self._initialize()
    
    def _show_error(self):
        if self._notification_label : self._notification_label.destroy()
        self._notification_label = Label(
            master=self._frame,
            text="Virheellinen syöte!",
            bg='white',
            foreground='red'
        )
        self._notification_label.grid(column=1, padx=5, pady=5)
    
    def _show_success(self):
        if self._notification_label : self._notification_label.destroy()
        self._notification_label = Label(
            master=self._frame,
            text="Uusi tapahtuma lisätty!",
            bg="white",
            foreground='green'
        )
        self._notification_label.grid(column=1, padx=5, pady=5)

    def pack(self):
        self._frame.pack(fill='both')

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(master=self._parent, bg='white')
        val = IntVar()
        
        event_type_label = Label(
            master=self._frame,
            text="Valitse tyyppi:",
            bg='white'
        )
        sale_event_radiobutton = Radiobutton(
            master=self._frame,
            text="Myynti",
            variable=val,
            value=1,
            bg='white',
            highlightthickness=0
        )
        expense_event_radiobutton =Radiobutton(
            master=self._frame,
            text="Osto",
            variable=val,
            value=2,
            bg='white',
            relief='flat',
            highlightthickness=0,
            state=DISABLED
        )
        amount_label = Label(
            master=self._frame,
            text="Summa:",
            bg='white'
        )
        amount_entry = Entry(
            master=self._frame
        )
        description_label = Label(
            master=self._frame,
            text='Kuvaus:',
            bg='white'
        )
        description_entry = Entry(
            master=self._frame
        )

        create_event_button = Button(
            master=self._frame,
            text="Lisää tapahtuma",
            command=lambda : add_event(),
            bg='white'
        )

        def add_event():
            user_id = self._user.id
            try :
                amount = float(amount_entry.get().replace(",","."))
            except : 
                self._show_error()
                return
            description = description_entry.get()
            if amount < 0 or len(description) == 0:
                self._show_error()
                return
            amount_in_sents = int(amount * 100)
            self._sales_repository.create(description, amount_in_sents, user_id, 0)
            amount_entry.delete(0, END)
            description_entry.delete(0, END)
            self._show_success()
            

        event_type_label.grid(row=0, column=0, padx=5, pady=5)
        sale_event_radiobutton.grid(row=0, column=1, padx=5, sticky='w')
        expense_event_radiobutton.grid(row=1, column=1, padx=5, sticky='w')
        amount_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        amount_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        description_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        description_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        create_event_button.grid(row=4, column=1, padx=5, pady=5, sticky='w')

    
class Statistics:

    def __init__(self, parent, user : User, sales_repository : SalesRepository) -> None:
        self._parent =parent
        self._user = user
        self._sale_repository = sales_repository
        self._frame = None
    
        self._initialize()
        
    def pack(self):
        self._frame.pack(fill='both')
        
    def destroy(self):
        self._frame.destroy()
        
    def _initialize(self):
        self._frame = Frame(master=self._frame, bg='white')
        self._frame.grid_columnconfigure(0, minsize=640)

        total_sales = self._sale_repository.total_amount(self._user.id) / 100.0
        overview_label =Label(
            master=self._frame,
            text = f"YHTEENVETO\tMYYNNIT: {total_sales:.2f} euroa",
            bg='white'
        )

        sales_label = Label(
            master=self._frame,
            text="MYYNNIT",
            bg='white',
            font=('monospace', 12, 'bold')
        )
        overview_label.grid(padx=5, pady=5, sticky='w')
        sales_label.grid(padx=5, pady=5, sticky='w')

        sales = self._sale_repository.get_all_sale_rows(self._user.id)

        row_index = 1
        for sale in sales:
            amount_in_euros = sale.amount / 100.0
            desc = sale.description
            row_as_str = f"{row_index}."
            sale_row_label = Label(
                master=self._frame,
                text=f"{row_as_str:10}{amount_in_euros:<15.2f}{desc}",
                bg='white'
            )
            sale_row_label.grid(padx=5, sticky='w')
            row_index += 1
