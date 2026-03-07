from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# lam - rate or known number of occurrences e.g. 2 for above problem.

# size - The shape of the returned array.

x = random.poisson(lam=3, size=(5))
print(x)

sns.displot(random.poisson(lam=3, size=5))

plt.show()

# diff between normal and poisson
data = {
  "normal": random.normal(loc=50, scale=7, size=1000),
  "poisson": random.poisson(lam=50, size=1000)
}

sns.displot(data, kind="kde")

plt.show()

# diff between binomial and poisson
data = {
  "binomial": random.binomial(n=1000, p=0.01, size=1000),
  "poisson": random.poisson(lam=10, size=1000)
}

sns.displot(data, kind="kde")

plt.show()