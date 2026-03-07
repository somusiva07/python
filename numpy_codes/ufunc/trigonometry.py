import numpy as np

x = np.sin(np.pi/2)

print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x)

base = 3
perp = 4

x = np.hypot(base, perp)

print(x)