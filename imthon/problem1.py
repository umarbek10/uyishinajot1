def has_odd_occurrences(lst):
    from collections import Counter
    
    counts = Counter(lst)
    

    for count in counts.values():
        if count % 2 != 0:
            return True
    return False


example_list = [1, 2, 3, 2, 3, 3]
print(has_odd_occurrences(example_list))  

example_list = [1, 2, 3, 2, 3, 1]
print(has_odd_occurrences(example_list))  
