import csv

class PhonebookDAO:

    def __init__(self):
        self.phonebookData = []
    
    def gatherData(self):
        with open('data.csv', newline = '') as csvfile:
            Data = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
            for row in Data:
                print(' '.join(row))

