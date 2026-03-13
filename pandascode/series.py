# A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.

import pandas as pd 

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

print(pd.Series(calories, index = ["day1", "day2"]))