import numpy as np
from scipy import stats

# Sample data
marks = np.array([72, 75, 78, 70, 74, 77, 73, 76, 79, 75])

# One-sample t-test
t_stat, t_pvalue = stats.ttest_1samp(marks, popmean=70)

print("One-Sample t-Test")
print("t-statistic:", round(t_stat, 4))
print("p-value:", round(t_pvalue, 4))

# Z-test (population standard deviation is known)
population_mean = 70
population_std = 5
sample_mean = np.mean(marks)
n = len(marks)

z_stat = (sample_mean - population_mean) / (population_std / np.sqrt(n))
z_pvalue = 2 * (1 - stats.norm.cdf(abs(z_stat)))

print("\nZ-Test")
print("z-statistic:", round(z_stat, 4))
print("p-value:", round(z_pvalue, 4))

# Decision at the 5% significance level
alpha = 0.05

if t_pvalue < alpha:
    print("\nT-Test Decision: Reject H0")
else:
    print("\nT-Test Decision: Fail to reject H0")

if z_pvalue < alpha:
    print("Z-Test Decision: Reject H0")
else:
    print("Z-Test Decision: Fail to reject H0")
