# Q100. Write a python program to print below pattern.
# ```
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 
# ```
l=['A','B','C','D','E']
for i in range(1,5+1):
    for j in range(1,5+1):
        if(i>=j):
            print(l[i-1],end=' ')
    print()