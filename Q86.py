#Write a Python program to check if a string is palindrome or not
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

word = "level"
result = is_palindrome(word)

if result:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
