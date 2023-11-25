#Write a Python program to convert a list of tuples into dictionary.
#Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
#Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
def tuples_to_dict(list_of_tuples):
    return dict(list_of_tuples)

input_list = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]

output_dict = tuples_to_dict(input_list)
print( output_dict)
