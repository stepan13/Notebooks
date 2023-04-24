from Notebook import Notebook 
class UserFilter:

    def __init__(self,dataBase) -> None:
        self.userHere = True
        self.base = set()
        self.filterBase = set()
        self.filter = Notebook()
        self.base = set(dataBase)

    def printOptions(self):
        print("0 - exit")
        print("1 - model (" + self.filter.getOption("model") + ")")
        print("2 - RAM (" + str(self.filter.getOption("ram")) + ")")
        print("3 - disk (" + str(self.filter.getOption("disk")) + ")")

    def askFilter(self):
        self.printOptions()
        userChoice = int(input("Option: "))
        if(userChoice == 0):
            self.userHere = False
            return
        else: self.askOption(userChoice)
        self.runFilter()
        self.printFilter()

    def askOption(self,userChoice):
        if(userChoice == 1): 
            optionName = "model"
            value = str(input("model: "))
        elif(userChoice == 2): 
            value = int(input("RAM: "))
            optionName = "ram"
        elif(userChoice == 3): 
            value = int(input("Disk: "))
            optionName = "disk"
        self.filter.setOption(optionName,value)

    def runFilter(self):
        self.filterBase = self.base.copy()
        self.filterByRam()
        self.filterBydisk()
        self.filterByModel()
    
    def filterByRam(self):
        self.filterByOption("ram")
    def filterBydisk(self):
        self.filterByOption("disk")
    def filterByModel(self):
        self.filterByOption("model")
    
    def filterByOption(self,optionName):
        for item in self.base:
            if item in self.filterBase:
                if self.filter.compare(item,optionName):
                    self.filterBase.remove(item)

    def printFilter(self):
        for i in self.filterBase:
            print(i)
    def printbase(self):
        for i in self.base:
            print(i)