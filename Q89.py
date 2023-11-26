#Write a Python program to find words which are greater than given length k.
def words_greater_than_k(string, k):
    words = string.split()
    result = [word for word in words if len(word) > k]
    return result

text = "This is a sample sentence to demonstrate the functionality"
length = 4
long_words = words_greater_than_k(text, length)
print(long_words)
