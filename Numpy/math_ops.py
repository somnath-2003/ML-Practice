import numpy as np

#-------Square Root------

a=9
arr=[1,4,9]
arr1=np.array(arr)
arr3=np.array([1,2,3,4])
print(np.sqrt(a))
print(np.sqrt(arr))
print(np.sqrt(arr1))

#---Power---
print(np.power(2,3))
print(2**3)
print(np.power(arr1,0.5))
print(arr1**0.5)
print(np.power(arr1,arr))
print(arr1**arr)

# -----Exponential-----
print(np.exp(2)) #e^2
print(np.exp(arr3))


#----Logarithm-------
arr4=np.array([1,2,8,16])
arr5=np.array([1,10,100,1000])

print(np.log(10))#base e
print(np.log10(arr5))#base 10
print(np.log2(arr4))#base 2
tiny_value=1e-12
print(np.log1p(tiny_value))#for tiny values

#------Trignometric Functions---------
arr6=[0.,np.pi/6,np.pi/4,np.pi/3,np.pi/2,np.pi*2/3,np.pi]
print(np.sin(arr6))
print(np.cos(arr6))
print(np.tan(arr6))
print(np.tan(np.pi/2))

#---Inverse Trignometic Functions-----
arr7=np.array([0,0.5,1,-1])
print(np.arcsin(arr7))
print(np.arccos(arr7))
print(np.arctan(arr7))

#---Degree Radian Conversion-----
arr8=[0,30,60,90,180,270,360]
arr9=np.deg2rad(arr8)
print("arr9= ",arr9)
print(np.rad2deg(arr9))

#------Rounding & related functions-----
arr10=[0,0.45,1.50,3.3,4.50,5.67,-1.55,-2.7,-3.34,-4.5]
print(np.round(arr10))#.5 round to nearest even value
print(np.round(arr10,1))#round upto 1 decimal value

print(np.ceil(arr10))#round towards +Infinity
print(np.floor(arr10))#round towards -Infinity
print(np.trunc(arr10))#rounds towards 0,it removes the decimal part

