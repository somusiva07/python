import numpy as np

array1 = np.array([5,10,15,20,25])
array2 = np.array([2,4,6,8,10])

sum = np.sum(array1)

print(sum)

sum1 = np.sum([array1,array2])

print(sum1)

cumsum = np.cumsum(array2)

print(cumsum)

