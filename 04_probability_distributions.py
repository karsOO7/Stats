import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Binomial distribution
binomial_data = np.random.binomial(n=10, p=0.5, size=1000)

plt.figure()
plt.hist(binomial_data, bins=np.arange(-0.5, 11.5, 1), edgecolor="black")
plt.xlabel("Number of Successes")
plt.ylabel("Frequency")
plt.title("Binomial Distribution")
plt.tight_layout()
plt.show()

# Normal distribution
normal_data = np.random.normal(loc=50, scale=10, size=1000)

plt.figure()
plt.hist(normal_data, bins=30, edgecolor="black")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Normal Distribution")
plt.tight_layout()
plt.show()
