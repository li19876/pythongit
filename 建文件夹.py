import os
import easygui as e
import numpy
dirs = e.diropenbox()
res=list(os.walk(dirs))
newlist=numpy.array_split(res[0][2],286)
print(len(newlist))
