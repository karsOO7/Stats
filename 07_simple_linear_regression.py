import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# House area in square feet
area = np.array([1000, 1200, 1500, 1800, 2000, 2200]).reshape(-1, 1)

# House price in lakhs
price = np.array([50, 58, 70, 82, 90, 100])

# Create and train the model
model = LinearRegression()
model.fit(area, price)

# Predictions
predicted_price = model.predict(area)

# Model parameters
slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(area, price)

print("Slope:", round(slope, 4))
print("Intercept:", round(intercept, 4))
print("R² Value:", round(r2, 4))

# Plot actual observations and fitted regression line
plt.figure()
plt.scatter(area.ravel(), price, label="Actual Data")
plt.plot(area.ravel(), predicted_price, label="Regression Line")
plt.xlabel("Area (sq. ft.)")
plt.ylabel("Price (Lakhs)")
plt.title("House Price Prediction using Linear Regression")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
