from Database import Database
from Notebook import Notebook
from UserFilter import UserFilter


data = Database()
for i in range(0,10):
    data.addNew(data.createRandom())

filter = UserFilter(data.base)
filter.printbase()
while filter.userHere:
    filter.askFilter()



