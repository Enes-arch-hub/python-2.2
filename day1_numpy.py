import numpy as np

# 1. Create arrays
numbers = np.array([10, 20, 30, 40, 50])

print("Array:", numbers)
print("First:", numbers[0])
print("Last:", numbers[-1])

# 2. Arithmetic
print("\nArithmetic")
print(numbers + 5)
print(numbers * 2)
print(numbers ** 2)

# 3. Statistics
print("\nStatistics")
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Max:", np.max(numbers))
print("Min:", np.min(numbers))