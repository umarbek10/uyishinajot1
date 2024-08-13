def filter_integers(numbers, threshold):
    return list(filter(lambda x: x >= threshold, numbers))

# Example usage
numbers = [10, 5, 20, 3, 15, 8]
threshold = 10
filtered_numbers = filter_integers(numbers, threshold)
print(filtered_numbers)
