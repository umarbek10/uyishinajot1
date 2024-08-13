def transform_number(num):
    if num > 0:
        return -num
    else:
        return num - 2000000

def transform_list(numbers):
    return list(map(transform_number, numbers))


numbers = [500000, -100000, 0, 3000000, -500000]
transformed_numbers = transform_list(numbers)
print(transformed_numbers)
