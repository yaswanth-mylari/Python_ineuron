#Write a Python program to remove i'th element from a string
def removeielement(st,i):
    return st[:i-1]+st[i:]
print(removeielement("asdasda", 3))