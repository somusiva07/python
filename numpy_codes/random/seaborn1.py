import matplotlib.pyplot as plt
import seaborn as sns

# Displot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.
# sns.displot([0, 1, 2, 3, 4, 5])

# plt.show()

sns.displot([0, 1, 2, 3, 4, 5], kind="kde")

plt.show()