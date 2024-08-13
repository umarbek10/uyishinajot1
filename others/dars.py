def combine_lists(ids, names, scores):
   
    combined_list = []

    for i in range(len(ids)):
       
        id = ids[i]
        name = names[i]
        score = scores[i]

        student_dict = {id: (name, score)}

        combined_list.append(student_dict)

    return combined_list

ids = ['S001', 'S002', 'S003', 'S004']
names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
scores = [85, 98, 89, 92]

result = combine_lists(ids, names, scores)
print(result)

s = 12;