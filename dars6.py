def sort_odd_even(numbers):
    # Toq va juft elementlarni ajratib olamiz
    odd_numbers = [x for x in numbers if x % 2 != 0]
    even_numbers = [x for x in numbers if x % 2 == 0]

    # Toq elementlarni o'sish tartibida tartiblaymiz
    odd_numbers.sort()
    # Juft elementlarni kamayish tartibida tartiblaymiz
    even_numbers.sort(reverse=True)

    # Natija uchun bo'sh list yaratamiz
    result = []
    odd_index = 0
    even_index = 0

    # Asosiy listni qayta yig'amiz
    for number in numbers:
        if number % 2 != 0:
            result.append(odd_numbers[odd_index])
            odd_index += 1
        else:
            result.append(even_numbers[even_index])
            even_index += 1
    
    return result

# Test uchun misollar
print(sort_odd_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # [1, 10, 3, 8, 5, 6, 7, 4, 9, 2]
