def digit_sum(number):

    while number >= 10:
        number = sum(int(digit) for digit in str(number))
    return number

print(digit_sum(38))  
print(digit_sum(96))  
print(digit_sum(12345)) 
print(digit_sum(9999)) 
