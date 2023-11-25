#Write a Python program to swap two elements in a list.
def swap(l,i,j):
    l[i],l[j]=l[j],l[i]
    return l
lst=[1,32,4,5,6]
print(swap(lst, 1 , 4))