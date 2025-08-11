"""
creating env1 environment:
conda create --name env1 python=3.13.5

activating env1:
conda activate env1

installing numpy:
conda install numpy


"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Mean of array:", np.mean(arr))
