def sort_odd_even(numbers):
    
    odd_numbers = [x for x in numbers if x % 2 != 0]
    even_numbers = [x for x in numbers if x % 2 == 0]

   
    odd_numbers.sort()
  
    even_numbers.sort(reverse=True)

   
    result = []
    odd_index = 0
    even_index = 0

    for number in numbers:
        if number % 2 != 0:
            result.append(odd_numbers[odd_index])
            odd_index += 1
        else:
            result.append(even_numbers[even_index])
            even_index += 1
    
    return result

print(sort_odd_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  
