import csv

class PhonebookDAO:

    def __init__(self):
        self.phonebook = []
    
    def gatherData(self):
        with open('data.csv', newline = '') as csvfile:
            Data = csv.reader(csvfile, delimiter = ',', quotechar = '|')
            for row in Data:
                self.phonebook.append(row)
        
        return self.phonebook