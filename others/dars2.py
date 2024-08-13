def list_to_dict(nested_list):
    
    result_dict = {}
        
    for item in nested_list:
    
        key = item[0]
        value = item[1:]
        
        result_dict[key] = value
    
    return result_dict

nested_list = [
    [1, 'Jean Castro', 'V'],
    [2, 'Lula Powell', 'V'],
    [3, 'Brian Howell', 'VI'],
    [4, 'Lynne Foster', 'VI'],
    [5, 'Zachary Simon', 'VII']
]

result = list_to_dict(nested_list)
print(result)
