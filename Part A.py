import random

# Part A
die_faces = 6

# 1. Total combinations
total_combos = die_faces ** 2
print("Total combinations:", total_combos)

# Part B: Combinations Distribution
combinations_distribution = []

# Create a 6x6 matrix
for i in range(1, 7):
    row = []
    for j in range(1, 7):
        row.append(i + j)
    combinations_distribution.append(row)

# Display the matrix
print("\nCombinations Distribution:")
for row in combinations_distribution:
    print(row)

# Part C: Probability Distribution
probability_distribution = {}

# Calculate the probability for each sum
for i in range(2, 13):
    count = sum(row.count(i) for row in combinations_distribution)
    probability_distribution[i] = count / total_combos

# Display the probabilities
print("\nProbability Distribution:")
for sum_, prob in probability_distribution.items():
    print(f"P(Sum = {sum_}) = {prob:.4f}")
