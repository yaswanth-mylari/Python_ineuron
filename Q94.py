#Write a Python program to get all combinations of 2 tuples.
#Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
#Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
def combination(t1,t2):
    l1=[]
    l2=[]
    for i in t1:
        for j in t2:
            l1.append((i,j))
            l2.append((j,i))
    l1.extend(l2)
    return l1

l1=(7,2)
l2=(4,5)
print(combination(l1, l2))