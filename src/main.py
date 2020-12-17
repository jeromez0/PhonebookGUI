from tkinter import *
import UserInterface
import PhonebookDAO

if __name__ == "__main__":


    Data = PhonebookDAO.PhonebookDAO()
    Data.gatherData()

    root = Tk()
    root.title = ("Phonebook")
    Phonebook = UserInterface.UserInterface(root)
    root.mainloop()

