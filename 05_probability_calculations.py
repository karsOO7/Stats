import numpy as np

# Theoretical probability
outcomes = np.array([1, 2, 3, 4, 5, 6])

# Probability of getting an even number
even_outcomes = outcomes[outcomes % 2 == 0]
prob_even = len(even_outcomes) / len(outcomes)

# Probability of getting a number greater than 4
greater_than_four = outcomes[outcomes > 4]
prob_greater_four = len(greater_than_four) / len(outcomes)

print("Theoretical Probability:")
print("P(Even number) =", prob_even)
print("P(Number > 4) =", prob_greater_four)

# Simulation
np.random.seed(42)
rolls = np.random.randint(1, 7, size=10000)

experimental_even = np.sum(rolls % 2 == 0) / len(rolls)
experimental_greater_four = np.sum(rolls > 4) / len(rolls)

print("\nExperimental Probability:")
print("P(Even number) =", experimental_even)
print("P(Number > 4) =", experimental_greater_four)
