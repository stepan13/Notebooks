from random import Random
from Notebook import Notebook
class Database:

    def __init__(self) -> None:
        self.base = set()
        self.index = 0
    
    def addNew(self, item):
        self.base.add(item)
        self.index +=1
    def createRandom(self):
         ram = pow(2,1+Random().randint(0,7))
         disk = 1 + Random().randint(0,4)
         model = "model" + str(self.index+1)
         item = Notebook(model,ram,disk)
         return item
    
    def printbase(self):
        for i in self.base:
            print(i)