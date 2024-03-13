import random

def undoom_dice(die_A, die_B):
    # Example transformation for Die A, ensuring no face has more than 4 spots
    new_die_A = list(range(1, 7))
    random.shuffle(new_die_A)  # Shuffle new_die_A

    # Keep Die B unchanged
    new_die_B = [random.randint(1, 6) for _ in range(len(die_B))]  
    random.shuffle(new_die_B)  # Shuffle new_die_B

    return new_die_A, new_die_B

def get_probabilities(combinations):
    total_combinations = sum(combinations.values())
    probabilities = {sum_result: count / total_combinations for sum_result, count in combinations.items()}
    return probabilities

original_die_A = [1, 2, 3, 4, 5, 6]
original_die_B = [1, 2, 3, 4, 5, 6]

new_die_A, new_die_B = undoom_dice(original_die_A, original_die_B)

print("Original Die A:", original_die_A)
print("Original Die B:", original_die_B)
print("New Die A:", new_die_A)
print("New Die B:", new_die_B)

# Calculate probabilities after undooming
combinations_B = {}
for die_a in new_die_A:
    for die_b in new_die_B:
        sum_result = die_a + die_b
        if sum_result not in combinations_B:
            combinations_B[sum_result] = 0
        combinations_B[sum_result] += 1

probabilities_B = get_probabilities(combinations_B)
print("Probabilities B:")
for sum_result, prob in probabilities_B.items():
    print(f"{sum_result}: {prob:.4f}")