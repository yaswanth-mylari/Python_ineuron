#Write a Python program to extract unquire dictionary values.
def unique_dictionary_values(dictionary):
    unique_values = set()
    for value in dictionary.values():
        if isinstance(value, list):
            unique_values.update(value)
        else:
            unique_values.add(value)
    return list(unique_values)

sample_dict = {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': 'value1',
    'key4': 'value4'
}
unique_values = unique_dictionary_values(sample_dict)
print( unique_values)
