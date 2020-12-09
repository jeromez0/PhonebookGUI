from tkinter import *
import UserInterface





if __name__ == "__main__":
    root = Tk()
    root.title = ("Phonebook")

    Phonebook = UserInterface.UserInterface(root)
    root.mainloop()
