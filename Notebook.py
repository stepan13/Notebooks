

class Notebook:
    

    def __str__(self) -> str:
        result = ""
        for key, value in self.optionList.items():
            result = result + key + ": " + str(value) + " "
        return result

    def setOption(self,optionName,value):
        self.optionList[optionName] = value


    def __init__(self,model="", ram=0, disk=0) -> None:
        self.optionList = dict()
        self.setOption("model",model)
        self.setOption("ram",ram)
        self.setOption("disk",disk)
    

    def getOption(self,optionName):
        return self.optionList[optionName]
    
    def compare(self,o2, optionName):
        if optionName == "ram" or optionName == "disk":
            return self.getOption(optionName) >= o2.getOption(optionName)
        elif optionName == "model":
            model1 = self.getOption(optionName)
            model2 = o2.getOption(optionName)
            print(model1.find(model2))
            print(model2.find(model1))
            result = model2.find(model1) == -1
            return result

    
    
