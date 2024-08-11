def sort_by_length(strings):
    
    return sorted(strings, key=len)


input_list = ['Tarvuz', 'Nok', 'Olma']
output = sort_by_length(input_list)
print(output)  
