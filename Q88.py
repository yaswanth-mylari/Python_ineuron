#Write a Python program to check if a substring is present in a given string.
def check_substring(main_string, sub_string):
    if sub_string in main_string:
        return True
    else:
        return False
main_string = "Hello, how are you?"
sub_string = "how"
print(check_substring(main_string, sub_string))