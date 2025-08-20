import numpy as np
a=np.array([1,2,3,4,5])#1D array
print(a)
print("Datatype of a: ",a.dtype)
b= np.array([[1,2,3,4],[5,6,7,8]])#2D array
print("Datatype of b: ",b.dtype)

c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)
print(f"dimention of c: {c.ndim} Shape is:{c.shape} \n Data type of c:{c.dtype}")
#shape=(2,2,2)means two block each have 2 row 2 col
#print dimention
print("Dimention of a: ",a.ndim)
print("Dimention of b: ",b.ndim)

#shape
print("Shape(row*col of array) of a : ",a.shape)
print("Shape(order of the array) of b : ",b.shape)

#Float array
arr1=np.array([1.2,3.4,6.6])
print('Data type of arr1: ',arr1.dtype)
#force conversion of datatypes
arr2=arr1.astype(np.float32)
print("Data Type of arr2 :",arr2.dtype)
#float to int
arr3=arr1.astype(np.int32)
print(arr3)
print("datatype of arr3 : ",arr3.dtype)
#To get round off values from floating points
arr3=np.rint(arr1).astype(np.int32)
print(arr3)

#create differnt arrys
#filled with zeros
arr4=np.zeros((2,3))
print("arr4 \n:",arr4)
#filled with 1
arr5=np.ones((2,3))
print("arr5 \n:",arr5)
#filled with random garbage value
arr6=np.empty((2,3))
print("arr6 :\n",arr6)

#creat array from range
arr7=np.arange(10)
print("arr7:\n",arr7)

#reshape array
arr8=np.reshape(arr7,(2,5))#or you can use arr8=arr7.reshape(2,5)
print("arr8 :\n",arr8)
print(arr8.ndim)

#Using -1 for auto-calculation
arr9 = np.arange(12).reshape(3, -1)
print("\nAuto shaped arr9: (-1):\n", arr9)

#for higher dimensions
arr10 = np.arange(24)  # total elements = 24

reshaped = arr10.reshape(2, 3, -1)  # Let NumPy figure out last dimension
print(reshaped.shape)  
print(reshaped)

#Flattening of Multidimentional Arrays
#Flattening means turning a multi-dimensional array into a 1D array
arr11=np.array([[2,5,6],[7,3,1]])
flat_copy=arr11.flatten()
print("Flatted copy is \n",flat_copy)

# .ravel() also converts a multi-dimensional array into a 1D array, just like .flatten().
flat_view = arr11.ravel()
flat_view[0] = 99
print(flat_view)  # [2,5,6,7,3,1]
print(arr11)        # [[99,5,6] [ 7,3,1]] 

#Expand dimentions
newarr = np.array([1,2,3])
np.expand_dims(newarr, axis=0).shape  # (1,3)row vector
np.expand_dims(newarr, axis=1).shape  # (3,1)column vector

#Squeeze dimentions
newarr1 = np.array([[[1,2,3]]])   # shape (1,1,3)
print("Original shape:", newarr1.shape)

squeezed = np.squeeze(newarr1)
print("After squeeze shape:", squeezed.shape)  # (3,)








# Base array
arr12 = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print("Original array:\n", arr12)

# Indexing 
# arr12[0] = first row
print("\nFirst row:", arr12[0])        

# arr12[:, 1] = second column
print("Second column:", arr12[:, 1])   

# arr12[1, 2] -> element at row 2, col 3
print("Element at (2,3):", arr12[1, 2])  

# ----- Slicing -----
# Syntax: arr12[row_start:row_end:row_step, col_start:col_end:col_step]
# Example: take first 2 rows (0:2) and columns 1-2 (1:3)
print("\nSubarray (rows 0-1, cols 1-2):\n", arr12[0:2, 1:3])  

# ----- Reversing -----
# arr12[::-1] -> reverse rows
print("\nReverse rows:\n", arr12[::-1])

# arr12[:, ::-1] -> reverse columns
print("Reverse columns:\n", arr12[:, ::-1])

# arr12[::-1, ::-1] -> reverse rows & columns (180° rotation)
print("Reverse both (180° rotation):\n", arr12[::-1, ::-1])

# Extra slicing example: step slicing
print("\nEvery 2nd element in row 1:", arr12[0, ::2])  




#----Numpy arithmatics------

arr13=np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print("sum of all the elements of the numpy  array: ",arr13.sum())

print("adding 10 to every element: ",arr13 +10)
print("subtracting 10 to every element: ",arr13 -10)
print("multiplying 10 to every element: ",arr13 *10)
print("Dividing 10 to every element: ",arr13 /10)

arr14=np.array([[9,8,7],[6,5,4],[3,2,1]])
print("adding arr13 and arr14 elementwise :\n",arr13+arr14)
print("multipling arr13 and arr14 element by corresponding element :\n",arr13*arr14)#it is not matrix multiplication
#matrix multiplication
print("matrix multiplication of arr13 and  arr14 :\n",arr13 @ arr14)# or you can use np.matmul(arr13,arr14)
print("matrix multiplication of arr13 and  arr14 :\n",np.matmul(arr13,arr14))


#-----Aggregates------ WITHOUT AXIS-----------
print("sum of all the elements of the  array:",np.sum(arr13))
print("mean of arr3 :",np.mean(arr13))
print("standard deviation of arr13 : ",np.std(arr13))

#Find max and Min in Araay
print("Maximum element of arr13  :",np.max(arr13))
print("Minimum element of arr13 :",np.min(arr13))
#Find max and min between two arrays
print("array of Maximum element between arr13 and arr14 :",np.maximum(arr13,arr14))

A = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])  # shape (2,2,2)
B = np.array([[[9,8],[7,6]], [[5,4],[3,2]]])  # shape (2,2,2)

print(A + B)   # adds element by element

#----Aggregates------ WITH  AXIS (direction of aggregation)--------
print("sum of all the elements of the  array:",np.sum(arr13))
print("sum of  columns :",np.sum(arr13,axis=0))
print("sum of  rows :",np.sum(arr13,axis=1))
print("mean of arr13 columns :",np.mean(arr13,axis=0))
print("mean of arr13 rows :",np.mean(arr13,axis=1))
print("standard deviation of arr13 columns : ",np.std(arr13,axis=0))
print("standard deviation of rows :",np.std(arr13,axis=1))

#Find max and Min in Araay
print("Maximum element of each columns :",np.max(arr13,axis=0))
print("Maximum element of each rows :",np.max(arr13,axis=1))
print("Minimum element of each colums  :",np.min(arr13,axis=0))
print("Minimum element of each rows  :",np.min(arr13,axis=1))




