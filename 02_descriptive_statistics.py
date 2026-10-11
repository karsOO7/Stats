import numpy as np
from statistics import mode

# Dataset
marks = [45, 50, 55, 60, 60, 65, 70, 75, 80, 85]

# Calculate statistics
mean = np.mean(marks)
median = np.median(marks)
mode_value = mode(marks)
data_range = np.max(marks) - np.min(marks)
standard_deviation = np.std(marks)

print("Dataset:")
print(marks)

print("\nMean:", mean)
print("Median:", median)
print("Mode:", mode_value)
print("Range:", data_range)
print("Standard Deviation:", round(standard_deviation, 2))
