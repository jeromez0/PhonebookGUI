from tkinter import *


class UserInterface:

    def __init__(self, main):
        self.frame = Frame(main)
        self.frame.pack()
        #### Frame 1
        ## first name
        self.labelF = Label(self.frame, text = "First Name")
        self.labelF.grid(row = 0, column = 0, sticky = W)
        self.EntryF = Entry(self.frame)
        self.EntryF.grid(row = 0, column = 1, sticky = E)

        # last name
        self.labelL = Label(self.frame, text = "Last Name")
        self.labelL.grid(row = 1, column = 0, sticky = W)
        self.EntryL = Entry(self.frame)
        self.EntryL.grid(row = 1, column = 1, sticky = E)
        
        #### Frame 2
        # buttons
        self.frame2 = Frame(main)
        self.frame2.pack()
        self.b1 = Button(self.frame2, text = "  Add  ")
        self.b2 = Button(self.frame2, text = "Update")
        self.b3 = Button(self.frame2, text = "Delete")
        self.b4 = Button(self.frame2, text = " Load ")

        self.b1.grid(row = 0, column = 0)
        self.b2.grid(row = 0, column = 1)
        self.b3.grid(row = 0, column = 2)
        self.b4.grid(row = 0, column = 3)


if __name__ == "__main__":
    root = Tk()
    root.title = ("Phonebook")
    Phonebook = UserInterface(root)
    root.mainloop()
