import numpy as np 

# NumPy is used to work with arrays. The array object in NumPy is called ndarray.

# We can create a NumPy ndarray object by using the array() function.

arr = np.array([1,2,3,4,5])

# print(arr)

# print(type[arr])

# indexing

# print(arr[3])

# print(arr[2]+arr[3])

arr2D = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('5th element on 2nd row: ', arr2D[1, 4])

arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(arr3D[1, 0, 1])

# slicing

# print(arr[2:4])

# print(arr[2:])

# print(arr[:4])

# print(arr2D[1, 1:4])

# print(arr2D[0:2, 2])

# print(arr2D[0:2, 1:4])

# print(arr2D.shape)

# for x in arr2D:
#   for y in x:
#     print(y)

# for x in arr3D:
#   for y in x:
#     for z in y:
#       print(z)    

# for x in np.nditer(arr2D):
#   print(x)      

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arrStack = np.stack((arr1, arr2), axis=1)

# print(arrStack)

arrhstack = np.hstack((arr1, arr2))

# print(arrhstack)

arrvstack = np.vstack((arr1, arr2))

# print(arrvstack)

arrdstack = np.dstack((arr1, arr2))

# print(arrdstack)

x = np.where(arr==4)
print(x)

even = np.where(arr%2==0)
print(even)

gt2 = np.where(arr>2)
print(gt2)

mixed = np.array([3,6,2,1,7,9])
mixedSort = np.sort(mixed)
print(mixedSort)