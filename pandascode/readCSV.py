import pandas as pd
import matplotlib.pyplot as plt

input = pd.read_csv('data.csv')

print(input.to_string())

print(input.corr())

#plot

# input.plot()

#Specify that you want a scatter plot with the kind argument:

# input.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
input.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()


