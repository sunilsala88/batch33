


import numpy as np
l1=[[1,2,3],[4,5,6],[6,7,8]]
np1=np.array(l1)
print(np1)

np2=np.arange(10,19).reshape(3,3)
print(np2)

#indexing
print(np2[0,2])

#slicing
print(np2[1:3,0:2])
print(np2[1:,:2])