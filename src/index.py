from tkinter import Tk, font
from views.ui import UI

def main() :
    root = Tk()
    root.title('MyLedgers')
    root.geometry('640x480')
    root.configure(bg='white')
    font.nametofont("TkDefaultFont").configure(
        family="monospace",
        size=12
    )

    ui = UI(root)
    ui.start()
    root.mainloop()

if __name__ == '__main__' :
    main()