import numpy as np
#----Random Floats------
a=np.random.rand(5) #gives 5 random floats between 0-1
print(a)

b=np.random.rand(1,10)
print(b,b.shape,b.ndim)

c=np.random.uniform(1,5,7)#gives 7 random floats between 1-5
print(c)


#------Random Integers------

arr0=np.random.randint(5)#gives one random integers between 0-5
print(arr0)

arr1=np.random.randint(1,10,5)#gives 5 integers between  1-10
print(arr1)

arr2=np.random.randint(1,10,(2,3))#gives 2*3 matrix using random integers between 1-10
print(arr2)

#-----Normal Distribution----
arr3=np.random.randn(5)#gives a sample array of 5 with mean=0 and standard deviation=1 (standard normal distribution)
print(arr3)

arr4=np.random.randn(2,3)#gives a array of size(2,3) with mean=0 and standard deviation=1
print(arr4)

arr5=np.random.normal(10,3,10)#gives a normal distribution of 10 numbers with mean=10,s.d=3
print(arr5)

arr5=np.random.normal(10,3,(2,3))#gives a normal distribution of size(2,3) numbers with mean=10,s.d=3
print(arr5)

#-----Seeds------
#When you use functions like np.random.rand() or np.random.randint(),
#  they generate different numbers each run (because they are pseudo-random).
#But sometimes in ML/DL or experiments, you need your results to be reproducible →
#  meaning if you (or someone else) runs the same code again, they should get the same random numbers.


np.random.seed(0)#after this all the random functions generate same random numbers for everytime you run the code

print(np.random.rand(3))      # same 3 floats every run
print(np.random.randint(1,10,3))  # same 3 ints every run
print(np.random.randn(3))     # same 3 normal samples every run

np.random.seed(0)
x = np.random.randint(1, 10, 3)
print("Seed 0:", x)   

np.random.seed(42)
x = np.random.randint(1, 10, 3)
print("Seed 42:", x)  

np.random.seed(99)
x = np.random.randint(1, 10, 3)
print("Seed 99:", x)  

np.random.seed(1)  # set seed

m = np.random.randint(0, 10, 5)
n = np.random.randint(0, 10, 5)

print(m)
print(n)

np.random.seed(1)  # set seed
a = np.random.randint(0, 10, 5)
np.random.seed(1)  # set seed twice so randon generate the same numbers
b = np.random.randint(0, 10, 5)

print(a)
print(b)

#-----Shuffle vs Permutation

arr6=np.arange(10)
print("before suffle: ",arr6)
np.random.shuffle(arr6)
print("after suffle :",arr6)

print(np.random.permutation(arr6))#permutation gives a copy of the suffled array 