def factorial(n):
    # Check for edge cases
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1

    # Calculate factorial
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
print(factorial(7))  # Output: 120
print(factorial(9))  # Output: 6
