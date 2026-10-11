import pandas as pd
import matplotlib.pyplot as plt

# Create a real-world-style student-performance dataset
data = {
    "Study_Hours": [2, 3, 4, 5, 5, 6, 7, 8, 9, 10],
    "Attendance": [65, 70, 72, 78, 80, 82, 85, 88, 92, 95],
    "Assignment_Score": [55, 60, 65, 70, 72, 75, 80, 84, 88, 92],
    "Exam_Marks": [50, 55, 60, 65, 68, 72, 76, 82, 88, 94],
}

df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Correlation matrix
print("\nCorrelation Matrix:")
print(df.corr())

# Average, maximum, and minimum examination marks
print("\nAverage Exam Marks:", round(df["Exam_Marks"].mean(), 2))
print("Maximum Exam Marks:", df["Exam_Marks"].max())
print("Minimum Exam Marks:", df["Exam_Marks"].min())

# Histogram
plt.figure()
plt.hist(df["Exam_Marks"], bins=5, edgecolor="black")
plt.xlabel("Exam Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Examination Marks")
plt.grid(True)
plt.tight_layout()
plt.show()

# Scatter plot
plt.figure()
plt.scatter(df["Study_Hours"], df["Exam_Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Exam Marks")
plt.title("Study Hours vs Examination Marks")
plt.grid(True)
plt.tight_layout()
plt.show()
