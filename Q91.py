#Write a Python program to merge two dictionary
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dictionary1 = {'a': 1, 'b': 2}
dictionary2 = {'b': 3, 'c': 4}

print(merge_dictionaries(dictionary1, dictionary2))