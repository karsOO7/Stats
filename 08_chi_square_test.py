import numpy as np
from scipy.stats import chi2_contingency

# Contingency table
# Rows: Streams
# Columns: Participated, Not Participated
data = np.array([
    [30, 20],
    [25, 25],
    [35, 15],
])

# Perform Chi-Square test
chi2, p_value, degrees_of_freedom, expected = chi2_contingency(data)

print("Observed Frequencies:")
print(data)

print("\nChi-Square Statistic:", round(chi2, 4))
print("Degrees of Freedom:", degrees_of_freedom)
print("p-value:", round(p_value, 4))

print("\nExpected Frequencies:")
print(expected)

alpha = 0.05

if p_value < alpha:
    print("\nDecision: Reject H0")
    print("There is a significant association between the variables.")
else:
    print("\nDecision: Fail to reject H0")
    print("There is insufficient evidence of an association.")
