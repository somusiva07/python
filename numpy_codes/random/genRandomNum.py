from numpy import random

xInt = random.randint(63)

print(xInt)

xFloat = random.rand()

print(xFloat)

# Generate a 1-D array containing 5 random integers from 0 to 100:

xIntRand1D = random.randint(63, size=(5))

print(xIntRand1D)

# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:

xIntRand2D = random.randint(63, size=(3,5))

print(xIntRand2D)

# 2D float

xFloatRand2D = random.rand(3, 5)

print(xFloatRand2D)

# choice
# The sum of all probability numbers should be 1. Even if you run the example above 100 times, the value 9 will never occur.

xChoice = random.choice([3, 5, 7, 9], p=[0.7, 0.2, 0.1, 0.0], size=(100))

print(xChoice)