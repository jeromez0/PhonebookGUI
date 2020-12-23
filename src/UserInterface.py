from tkinter import *
import PhonebookDAO

class UserInterface:

    def __init__(self, main):

        self.phonebookDAO = PhonebookDAO.PhonebookDAO()
        self.phonebook = self.phonebookDAO.gatherData()
        
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
        self.labelP = Label(self.frame, text = "Phone #")
        self.labelP.grid(row = 2, column = 0, sticky = W)
        self.EntryP = Entry(self.frame)
        self.EntryP.grid(row = 2, column = 1, sticky = E, pady = 3, padx = 5)

        #### Frame 2
        # buttons
        self.frame2 = Frame(main)
        self.frame2.pack()
        self.b1 = Button(self.frame2, text = "  Add  ", command = self.addEntry)
        self.b2 = Button(self.frame2, text = "Update")
        self.b3 = Button(self.frame2, text = "Delete", command = self.deleteEntry)
        self.b4 = Button(self.frame2, text = " Clear", command = self.clearListBox)

        self.b1.grid(row = 0, column = 0, pady = 5)
        self.b2.grid(row = 0, column = 1, pady = 5)
        self.b3.grid(row = 0, column = 2, pady = 5)
        self.b4.grid(row = 0, column = 3, pady = 5)

        #### Frame 3
        # listbox widget
        self.frame3 = Frame(main)
        self.frame3.pack()
        self.lb = Listbox(self.frame3, height = 20, width = 40)
        self.lb.grid(row = 0, column = 0, pady = 10, padx = 20)
        #scrollbar widget
        self.sb = Scrollbar(self.frame3, orient = VERTICAL)
        self.sb.grid(row = 0, column = 1, sticky = N + S, pady = 10)
        #configuring listbox with scrollbar
        self.sb.configure(command = self.lb.yview)
        self.lb.configure(yscrollcommand = self.sb.set)

        # Update entries
        self.updateEntry()

    def addEntry(self):
        self.phonebook.append( [self.EntryF.get(), self.EntryL.get(), self.EntryP.get()] )
        length = len(self.phonebook) - 1
        leng = len(f"{self.phonebook[i][1]}, {self.phonebook[i][0]}")
        newL = 30 -leng
        string = "-"*newL
        self.lb.insert(END, f"{self.phonebook[length][1]}, {self.phonebook[length][0]} {string} {self.phonebook[length][2]}")

    def updateEntry(self):
        for i in range(len(self.phonebook)):
            length = len(f"{self.phonebook[i][1]}, {self.phonebook[i][0]}")
            newL = 30 -length
            string = "-"*newL
            self.lb.insert(END, f"{self.phonebook[i][1]}, {self.phonebook[i][0]} {string} {self.phonebook[i][2]}")

    def deleteEntry(self):
        # step 1 is to bind the function to the button
        # step 2 we need a method to figure out which element was selected based on index
        try: 
            POINTER = self._selection()
        except:
            return
        # step 3 we need to delete from memory (the list) at the index using list method 'del'            
        del self.phonebook[POINTER]
        # step 4 delete elements from the tkinter display
        self.lb.delete(POINTER, POINTER)
    
    def _selection(self):
        return int(self.lb.curselection()[0])

    def clearListBox(self):
        for x in range(len(self.phonebook)):
            self.lb.delete(0, END)
    