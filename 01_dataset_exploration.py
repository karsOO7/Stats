import pandas as pd

# Create a sample dataset
data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Study_Hours": [2, 4, 5, 6, 8],
    "Attendance": [70, 75, 80, 85, 90],
    "Marks": [55, 62, 68, 75, 88],
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nFirst five records:")
print(df.head())

print("\nNumber of rows and columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())
