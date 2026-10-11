import matplotlib.pyplot as plt

# Sample data
students = ["A", "B", "C", "D", "E", "F", "G", "H"]
marks = [45, 55, 60, 62, 68, 72, 80, 90]

# Histogram
plt.figure()
plt.hist(marks, bins=5, edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Histogram of Marks")
plt.tight_layout()
plt.show()

# Boxplot
plt.figure()
plt.boxplot(marks)
plt.ylabel("Marks")
plt.title("Boxplot of Marks")
plt.tight_layout()
plt.show()

# Bar chart
plt.figure()
plt.bar(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.tight_layout()
plt.show()
