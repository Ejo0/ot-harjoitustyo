import sqlite3
from tkinter import Tk, font
from views.ui import UI


def main():
    root = Tk()
    root.title('SimpleAccountingTool')
    root.geometry('1280x720')
    root.configure(bg='white')
    font.nametofont("TkDefaultFont").configure(
        family="monospace",
        size=12
    )

    user_interface = UI(root)
    user_interface.start()
    root.mainloop()


if __name__ == '__main__':
    try:
        main()
    except sqlite3.OperationalError:
        print("Error: database is not initialized or available")