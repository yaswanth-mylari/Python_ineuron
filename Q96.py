# Write a python program to print below pattern.
# ```
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
for i in range(5):
    for j in range(5):
        if(i>=j):
            print("*", end=" ")
    print()
