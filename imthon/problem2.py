import re

def num_different_numbers(word):

    numbers = re.findall(r'\d+', word)
    

    unique_numbers = set(int(num) for num in numbers)
    

    return len(unique_numbers)


word = "a123bc34d8ef34"
print(num_different_numbers(word))  

word = "leet1234code234"
print(num_different_numbers(word))  

word = "a1b01c001"
print(num_different_numbers(word))  
