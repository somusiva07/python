from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=1000), kind="kde")
x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)

plt.show()

# The curve of a Normal Distribution is also known as the Bell Curve because of the bell-shaped curve.