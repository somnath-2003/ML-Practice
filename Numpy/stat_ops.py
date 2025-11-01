import numpy as np
arr1=np.array([1,3,5,7,20])

print(np.mean(arr1))
print(np.median(arr1))
print(np.std(arr1))
print(np.var(arr1))
print(np.max(arr1))
print(np.min(arr1))
print(np.argmax(arr1))
print(np.argmin(arr1))

#Percentiles & Axis-wise Statistics:
arr2=np.array([1,2,3,4,5,6,7,8,9])
print(np.percentile(arr1,25))
print(np.percentile(arr1,50))
print(np.percentile(arr1,75))
print(np.percentile(arr1,100))
#25th percentile → 25% of values are below it: value = 3
#50th percentile → 50% (half) of values are below it: value = 5 (this is also the median)
#75th percentile → 75% below it: value = 7

#quantiles:(np.percentile(arr, p) ≡ np.quantile(arr, p/100))

print(np.quantile(arr2,0.25))
print(np.quantile(arr2,0.50))
print(np.quantile(arr2,0.75))
print(np.quantile(arr2,1))

#Axis-wise Statistics
arr3=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr3.mean(axis=0))
print(arr3.mean(axis=1))

