from tkinter import *
import UserInterface
import PhonebookDAO

if __name__ == "__main__":

    root = Tk()
    root.title = ("Phonebook")
    Phonebook = UserInterface.UserInterface(root)
    root.mainloop()

