#Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
#Input: list = [9, 5, 6]
#Output: [(9, 729), (5, 125), (6, 216)]
def number_and_cube(input_list):
    return [(num, num ** 3) for num in input_list]

given_list = [9, 5, 6]
result = number_and_cube(given_list)
print( result)
