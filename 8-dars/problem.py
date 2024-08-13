import pandas as pd

data = pd.read_csv('product_material.txt')

filtered_data = data[(data['price'] >= 500) & (data['price'] <= 1000) & (data['is_available'] == True)]
result_1 = filtered_data[['id', 'material']]

print("Products with price between 500 and 1000 and available in the warehouse:")
print(result_1)

material_name = input("Enter the name of the material: ")

filtered_material_data = data[(data['material'] == material_name) & (data['is_available'] == True)]
result_2 = filtered_material_data[['price']].sort_values(by='price')

print(f"Prices of all products made of {material_name} that are currently available in the warehouse in ascending order:")
print(result_2);