import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[3,2],[6,5],[0,1]])
print("Matrix multiplication of two array: \n",np.dot(arr1, arr2))#for 2D matrix multiplication
print(arr1@arr2)#for Higher dimentions

#Transpose
print("Transpose: \n",arr2.T)
print(np.transpose(arr2))
a=  np.array([[2, 3, 1],
              [4, 5, 6],
              [7, 8, 9]])
#Diterminant
print("Diterminant :\n",np.linalg.det(a))
#if Diterminant=0 ,inverse does not exist
#Inverse
print("Inverse: \n",np.linalg.inv(a))

#(A*A^-1=Identity matrix)
print(a@np.linalg.inv(a))


