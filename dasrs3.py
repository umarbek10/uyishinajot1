def count_unique_numbers(numbers):
   
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    
  
    unique_count = sum(1 for count in counts.values() if count == 1)
    
    
    if unique_count == 0:
        return -1
    else:
        return unique_count

print(count_unique_numbers([4, 1, 2, 1, 2])) 
print(count_unique_numbers([1, 2, 3, 1, 1])) 
print(count_unique_numbers([1, 1, 1, 1]))    
print(count_unique_numbers([1, 2, 3, 4]))    
