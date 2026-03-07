from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.binomial(10,0.5,10), kind="kde")
x = random.binomial(n=10, p=0.5, size=(1))
print(x)

plt.show()

# The curve of a Normal Distribution is also known as the Bell Curve because of the bell-shaped curve.


data = {
  "normal": random.normal(loc=50, scale=5, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data, kind="kde")

plt.show()