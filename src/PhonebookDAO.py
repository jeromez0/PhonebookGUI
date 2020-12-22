import csv

class PhonebookDAO:

    def __init__(self):
        self.phonebookData = []
    
    def gatherData(self):
        with open('data.csv', newline = '') as csvfile:
            Data = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
            for row in Data:
                self.phonebookData.append(' '.join(row))
            
        print(self.phonebookData)


newPhonebook = PhonebookDAO()

newPhonebook.gatherData()