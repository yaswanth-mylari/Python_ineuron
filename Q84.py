#Write a Python program to find N largest element from a list.
def nthlargest(l,n):
    if(n>0 and n<=len(l)):
        l.sort(reverse=True)
        return(l[n-1])
    else:
        return "invalid input"
l=[1,2,4,3,5]
print(nthlargest(l, 3))