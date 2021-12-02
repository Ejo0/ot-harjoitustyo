from tkinter import *
from models.user import User
from services.accounting_service import AccountingService
from services.expense_row_service import ExpenseRowService
from services.sale_row_service import SaleRowService
from datetime import date

class UserView:

    def __init__(self, parent, user : User, show_home_view) -> None:
        self._parent = parent
        self._user = user
        self._show_home_view = show_home_view
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
        self._body = NewEvent(self._parent, self._user)
        self._body.pack()
    
    def _show_statistics(self):
        self._hide_body()
        self._body = Statistics(self._parent, self._user)
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

    def __init__(self, parent, user : User) -> None:
        self._parent = parent
        self._user = user
        self._sale_row_service = SaleRowService()
        self._expense_row_service = ExpenseRowService()
        self._frame = None
        self._notification_label = None

        self._initialize()
    
    def _show_error(self, message: str):
        if self._notification_label : self._notification_label.destroy()
        self._notification_label = Label(
            master=self._frame,
            text=message,
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
        event_type_variable = IntVar()
        vat_variable = StringVar()

        event_type_label = Label(
            master=self._frame,
            text="Valitse tyyppi:",
            bg='white'
        )
        sale_event_radiobutton = Radiobutton(
            master=self._frame,
            text="Myynti",
            variable=event_type_variable,
            value=1,
            bg='white',
            highlightthickness=0
        )
        expense_event_radiobutton =Radiobutton(
            master=self._frame,
            text="Osto",
            variable=event_type_variable,
            value=2,
            bg='white',
            relief='flat',
            highlightthickness=0
        )
        date_label = Label(
            master=self._frame,
            text='Päivämäärä:',
            bg='white'
        )
        date_entry = Entry(
            master=self._frame
        )
        amount_label = Label(
            master=self._frame,
            text="Summa (sis. alv):",
            bg='white'
        )
        amount_entry = Entry(
            master=self._frame
        )
        vat_label = Label(
            master=self._frame,
            text='Valitse alv-kanta:',
            bg='white'
        )
        vat_options = ['24%', '14%', '10%', '0%']
        vat_optionmenu = OptionMenu(
            self._frame,
            vat_variable,
            *vat_options,
        )
        vat_optionmenu.config(
            bg='white',
            activebackground='white',
            relief='flat',
            borderwidth=0,
            highlightthickness=0
        )
        vat_optionmenu['menu'].config(
            bg='white'
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
            try:
                event_date = date_entry.get()
                day, month, year = event_date.split(".")
                event_date_as_date = date(int(year), int(month), int(day))
            except:
                self._show_error("Syötä päiväys muodossa 1.1.2021")
                return
            try:
                amount = float(amount_entry.get().replace(",","."))
            except: 
                self._show_error("Tarkista summa")
                return
            if amount <= 0:
                self._show_error("Tarkista summa")
                return
            description = description_entry.get()
            if len(description) == 0 or len(description) > 50:
                self._show_error("Kuvauksen pituuden tulee olla 1-50 merkkiä")
                return

            amount_in_sents = int(amount * 100)

            vat = 0
            if vat_variable.get() == '24%' : vat = 24
            if vat_variable.get() == '14%' : vat = 14
            if vat_variable.get() == '10%' : vat = 10
            
            if event_type_variable.get() == 1 :
                self._sale_row_service.create_sale_row(user_id, event_date_as_date, amount_in_sents, vat, description)

            if event_type_variable.get() == 2 :
                self._expense_row_service.create_expense_row(user_id, event_date_as_date, amount_in_sents, vat, description)
            
            amount_entry.delete(0, END)
            description_entry.delete(0, END)
            date_entry.delete(0, END)
            self._show_success()
            

        event_type_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        sale_event_radiobutton.grid(row=0, column=1, padx=5, sticky='w')
        expense_event_radiobutton.grid(row=1, column=1, padx=5, sticky='w')
        date_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        date_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        amount_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        amount_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        vat_label.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        vat_optionmenu.grid(row=4, column=1, padx=5, pady=5, sticky='w')
        description_label.grid(row=5, column=0, padx=5, pady=5, sticky='w')
        description_entry.grid(row=5, column=1, padx=5, pady=5, sticky='w')
        create_event_button.grid(row=6, column=1, padx=5, pady=5, sticky='w')
        event_type_variable.set(1)
        vat_variable.set(vat_options[0])


class Statistics:

    def __init__(self, parent, user : User) -> None:
        self._parent =parent
        self._user = user
        self._accounting_service = AccountingService()
        self._sale_row_service = SaleRowService()
        self._expense_row_service = ExpenseRowService()
        self._frame = None
    
        self._initialize()
    
    def pack(self):
        self._frame.pack(fill='both', expand=1)
        
    def destroy(self):
        self._frame.destroy()
        
    def _initialize(self):
        self._frame = Frame(master=self._parent, bg='white')
        bookkeeping_text = Text(
            master=self._frame,
            bg='white',
        )
        total_sales = self._accounting_service.total_sales_including_vat(self._user.id) / 100.0
        total_expenses = self._accounting_service.total_expenses_including_vat(self._user.id) / 100.0
        net_sales = self._accounting_service.net_sales(self._user.id) / 100.0
        net_expenses = self._accounting_service.net_expenses(self._user.id) / 100.0
        net_result = self._accounting_service.net_result(self._user.id) / 100.0
        vat_on_sales = self._accounting_service.vat_on_sales(self._user.id) / 100.0
        deductible_vat = self._accounting_service.deductible_vat(self._user.id) / 100.0
        vat_payable = self._accounting_service.vat_payable(self._user.id) / 100.0


        overview_label =Label(
            master=self._frame,
            text =
                f"KASSAVIRTA\nMyynnit (sis. alv): {total_sales:.2f} euroa\n" +
                f"Ostot (sis. alv): {total_expenses:.2f} euroa\n\n" +
                f"TULOS- JA ALV-LASKELMA\nLiikevaihto: {net_sales:.2f} euroa\n" +
                f"Kulut: {net_expenses:.2f} euroa\n" +
                f"Tulos: {net_result:.2f} euroa\n\n" +
                f"Myynnin alv: {vat_on_sales:.2f} euroa\n" +
                f"Vähennettävä alv: {deductible_vat:.2f} euroa\n" +
                f"Verolle suoritettava alv: {vat_payable:.2f} euroa\n",
            bg='white',
            justify='l',
            anchor='w'
        )
        overview_label.pack(fill='both')

        bookkeeping_scrollbar = Scrollbar(
            bookkeeping_text,
            orient=VERTICAL,
            bg='black',
            troughcolor='white',
            highlightthickness=0,
            borderwidth=0,
        )

        sales = self._sale_row_service.rows_sorted_by_date(self._user.id)
        expenses = self._expense_row_service.rows_sorted_by_date(self._user.id)
        sales_header = f"{'MYYNNIT':10}{'Nro.':10}{'Pvm.':15}{'Summa (alv0)':>15}{'Alv':>15}{'Yht':>21}{'':10}{'Kuvaus'}\n"
        expenses_header = f"{'OSTOT':10}{'Nro.':10}{'Pvm.':15}{'Summa (alv0)':>15}{'Alv':>15}{'Yht':>21}{'':10}{'Kuvaus'}\n"

        bookkeeping_text.insert(END, sales_header)
        bookkeeping_text.tag_add('sales_header', '1.0', '1.end')
        bookkeeping_text.tag_config('sales_header', font='monospace 10 bold')
        row_index = 1
        for sale in sales:
            row_num_as_str = f"{row_index}."
            date_as_str = f"{sale.date.day:02d}.{sale.date.month:02d}.{sale.date.year}"
            vatless_amount = self._accounting_service.vatless_amount(sale) / 100.0
            vat_amount = self._accounting_service.vat_amount(sale) / 100.0
            amount_in_euros = sale.amount / 100.0
            if sale.vat == 0 : vat_percentage = f"({sale.vat}%) "
            else: vat_percentage = f"({sale.vat}%)"
            desc = sale.description
            sale_row_text = f"{'':10}{row_num_as_str:10}{date_as_str:<15}{vatless_amount:>15.2f}{vat_amount:>15.2f} {vat_percentage}{amount_in_euros:>15.2f}{'':10}{desc}\n"
            bookkeeping_text.insert(END, sale_row_text)
            row_index += 1
        
        bookkeeping_text.insert(END, "\n" + expenses_header)
        bookkeeping_text.tag_add('expenses_header', f'{row_index + 2}.0', f'{row_index + 2}.end')
        bookkeeping_text.tag_config('expenses_header', font='monospace 10 bold')
        row_index = 1
        for expense in expenses:
            row_num_as_str = f"{row_index}."
            date_as_str = f"{expense.date.day:02d}.{expense.date.month:02d}.{expense.date.year}"
            vatless_amount = self._accounting_service.vatless_amount(expense) / 100.0
            vat_amount = self._accounting_service.vat_amount(expense) / 100.0
            amount_in_euros = expense.amount / 100.0
            if expense.vat == 0 : vat_percentage = f"({expense.vat}%) "
            else: vat_percentage = f"({expense.vat}%)"
            desc = expense.description
            expense_row_text = f"{'':10}{row_num_as_str:10}{date_as_str:<15}{vatless_amount:>15.2f}{vat_amount:>15.2f} {vat_percentage}{amount_in_euros:>15.2f}{'':10}{desc}\n"
            bookkeeping_text.insert(END, expense_row_text)
            row_index += 1

        bookkeeping_text.config(yscrollcommand=bookkeeping_scrollbar.set)
        bookkeeping_scrollbar.config(command=bookkeeping_text.yview)

        bookkeeping_text.pack(fill='both', expand=1)
        bookkeeping_scrollbar.pack(side=RIGHT, fill=Y)