import math

def reduce_numbers(numbers):
    return list(map(math.floor, numbers))

numbers = [2.3, 3.7, 1.2, 4.9, 5.0, 6.8]
reduced_numbers = reduce_numbers(numbers)
print(reduced_numbers)
