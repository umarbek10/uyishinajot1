import math

def round_up_numbers(numbers):
    return list(map(math.ceil, numbers))

numbers = [2.3, 3.7, 1.2, 4.9, 5.0, 6.1]
rounded_numbers = round_up_numbers(numbers)
print(rounded_numbers)
