#Q95. Write a Python program to sort a list of tuples by second item.
#Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
#Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
def sort_tuples_by_second_item(input_list):
    return sorted(input_list, key=lambda x: x[1])

input_list = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
result = sort_tuples_by_second_item(input_list)
print( result)


    