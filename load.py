import numpy

class Load :
    def __init__(self, directory):
        self.address = directory
        self.samples_labels = self.loadData()


    def loadData(self):
        with open("iris.csv") as my_file:
            print(my_file.read())



