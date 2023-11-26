# Q99. Write a python program to print below pattern.
# ```
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# ```
for i in range(1,5+1):
    for j in range(1,5+1):
        if(i>=j):
            print(j,end=' ')
    print()