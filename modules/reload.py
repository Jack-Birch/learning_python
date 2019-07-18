import module1 
module1.spam('lit')

from importlib import reload      #This imports the reload function
reload(module1)             #This reloads the object module in memory 

#This can be useful when changes to the imported module have been made
#The module object it changed in place when reloaded