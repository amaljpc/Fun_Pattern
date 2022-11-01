import os
import numpy as np
from numpy import matrix

os.system("clear")

arr = [5,3,4,1]
columns = max(arr)
rows = len(arr)
mat = []
print(f"columns = {max(arr)} \nrows = {len(arr)}\n")
for i in arr:
    mat.append(i*'*'.split())


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
print(mat_Update)

arr_test = np.flipud(np.transpose(np.matrix(mat_Update))).tolist()

for i in arr_test:
    print('\t'.join(map(str, i)))
