from itertools import permutations

def largest_possible_number(numbers):
    str_numbers = list(map(str, numbers))
    
    all_permutations = permutations(str_numbers)
    
    max_number = 0
    
    for perm in all_permutations:
        current_number = int(''.join(perm))
        if current_number > max_number:
            max_number = current_number
    
    return max_number

print(largest_possible_number([1, 2, 3]))
print(largest_possible_number([61, 228, 9])) 
