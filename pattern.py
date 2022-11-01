import os
import numpy as np
import pandas as pd
from numpy import matrix

os.system("clear")

arr = [5,3,4,1]

columns,rows, mat = max(arr),len(arr),[]
[mat.append(i*'*'.split()) for i in arr]


mat_Update=[]
for i in range(0,len(mat)):
    temp = mat[i].copy()
    if len(mat[i])==columns:
        mat_Update.append(mat[i].copy())
    else:
        lis =[]
        [lis.append('') for i in range(0,(columns-len(mat[i])))]
        temp.extend(lis)
        mat_Update.append(temp)

df = pd.DataFrame(np.flipud(np.transpose(np.matrix(mat_Update))))
print(df)
