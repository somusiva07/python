import numpy as np 

num1 = 5
num2 = 7

print(np.lcm(num1,num2))

num1 = 11
num2 = 22

print(np.gcd(num1,num2))

arr = np.array([3, 6, 9, 18, 24, 27])

print(np.lcm.reduce(arr))

print(np.gcd.reduce(arr))