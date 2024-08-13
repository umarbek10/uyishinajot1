def count_increasing_sublists(numbers):
    if not numbers:
        return 0

   
    count = 0
    
    in_increasing_sequence = False
    

    prev = numbers[0]
    
    for num in numbers[1:]:
        if num > prev:
            
            if not in_increasing_sequence:
                count += 1
                in_increasing_sequence = True
        else:
            
            in_increasing_sequence = False
        
        
        prev = num
    
    return count

print(count_increasing_sublists([1, 3, 4, 9, 3, 4, -1, 7, 8])) 
print(count_increasing_sublists([1, 2, 3, 4, 5, 6]))
print(count_increasing_sublists([5, 4, 3, 2, 1]))  
print(count_increasing_sublists([1, 2, 1, 2, 1, 2, 1, 2])) 
