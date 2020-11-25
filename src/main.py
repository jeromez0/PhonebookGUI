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
        self.EntryF.grid(row = 0, column = 1, sticky = E, pady = 3, padx = 5)

        # last name
        self.labelL = Label(self.frame, text = "Last Name")
        self.labelL.grid(row = 1, column = 0, sticky = W)
        self.EntryL = Entry(self.frame)
        self.EntryL.grid(row = 1, column = 1, sticky = E, pady = 3, padx = 5)
        
        # phonebook
        self.labelL = Label(self.frame, text = "Phone #")
        self.labelL.grid(row = 2, column = 0, sticky = W)
        self.EntryL = Entry(self.frame)
        self.EntryL.grid(row = 2, column = 1, sticky = E, pady = 3, padx = 5)

        #### Frame 2
        # buttons
        self.frame2 = Frame(main)
        self.frame2.pack()
        self.b1 = Button(self.frame2, text = "  Add  ")
        self.b2 = Button(self.frame2, text = "Update")
        self.b3 = Button(self.frame2, text = "Delete")
        self.b4 = Button(self.frame2, text = " Load ")

        self.b1.grid(row = 0, column = 0, pady = 5)
        self.b2.grid(row = 0, column = 1, pady = 5)
        self.b3.grid(row = 0, column = 2, pady = 5)
        self.b4.grid(row = 0, column = 3, pady = 5)

        #### Frame 3
        # listbox widget
        self.frame3 = Frame(main)
        self.frame3.pack()
        self.lb = Listbox(self.frame3, height = 10)
        self.lb.grid(row = 0, column = 0, pady = 10)
        self.lb.insert(END, "entry1")
        self.lb.insert(END, "entry2")
        self.lb.insert(END, "entry3")
        self.lb.insert(END, "entry4")
        self.lb.insert(END, "entry5")
        self.lb.insert(END, "entry6")
        self.lb.insert(END, "entry7")
        self.lb.insert(END, "entry8")
        self.lb.insert(END, "entry9")
        self.lb.insert(END, "entry10")
        self.lb.insert(END, "entry11")

        #scrollbar widget
        self.sb = Scrollbar(self.frame3, orient = VERTICAL)
        self.sb.grid(row = 0, column = 1, sticky = N + S, pady = 10)

        #configuring listbox with scrollbar
        self.sb.configure(command = self.lb.yview)
        self.lb.configure(yscrollcommand = self.sb.set)


if __name__ == "__main__":
    root = Tk()
    root.title = ("Phonebook")
    Phonebook = UserInterface(root)
    root.mainloop()
