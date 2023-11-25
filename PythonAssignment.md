## Assignment Part-1
Q1. Why do we call Python as a general purpose and high-level programming language?
Ans: Python is called as general purpose programming language as it is used to develop applications etc. And is a high-level programming language as it is human understandable/readable.

Q2. Why is Python called a dynamically typed language?
Ans: Python is called a dynamically typed language as we no need to declare type of variable, type will be determined at runtime.

Q3. List some pros and cons of Python programming language?
Ans: 
Pros:
1. Simple and easily understandable (as simple as english)
2. Vast libraries (Supports database, Machine learning etc)
Cons:
1. Execution is slow compared to other highlevel languages
2. Not widely used for mobile app development

Q4. In what all domains can we use Python?
Ans:
1. Web applications
2. Data science
3. Database interactions

Q5. What are variable and how can we declare them?
Ans: Variable is a placeholder that holds value in memory.
    Declaration: 
    x=5
    y="hello"

Q6. How can we take an input from the user in Python?
Ans: x=input()

Q7. What is the default datatype of the value that has been taken as an input using input() function?
Ans: String

Q8. What is type casting?
Ans: Convert data from one type to another type

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?
Ans: No. But we can split the single value using split function which inturn give a list that contains multiple values
Ex:
values = input("Enter multiple values separated by space: ").split()
print("You entered:", values)

Q10. What are keywords?
Ans: Predefined words in any programming language. Can't use them for variables. 
Ex: for, in etc

Q11. Can we use keywords as a variable? Support your answer with reason.
Ans: No. 

Q12. What is indentation? What's the use of indentaion in Python?
Ans: Indentation is a kind of a tab space. All the code with same indentation belongs to same block/loop of code

Q13. How can we throw some output in Python?
Ans: Using print()

Q14. What are operators in Python?
Ans: Operators are symbols that perform some operation between variables

Q15. What is difference between / and // operators?
Ans: /= Division; //= Floor division
result_div = 7 / 2   # result_div is 3.5
result_floor = 7 // 2   # result_floor is 3

Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```
Ans: x="iNeuron"
     for x in range(3):
        x+=x
    print(x)

Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
Ans:
    x=int(input())
    if(x%2==0):
        print("even")
    else:
        print("odd")

Q18. What are boolean operator?
Ans: True , False , not , and , or

Q19. What will the output of the following?
```
1 or 0

0 and 0

True and False and True

1 or 0 or 0
```
Ans: 
1 or 0= 1

0 and 0= 0

True and False and True= False

1 or 0 or 0= 1

Q20. What are conditional statements in Python?
Ans: If-elif-else

Q21. What is use of 'if', 'elif' and 'else' keywords?
Ans: If-> if initial condition pass
     elif-> if condition failed and we have one more condition
     else-> All the conditions are failed

Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
Ans:
    x=int(input())
    if(x>=18):
        print("I can vote")
    else:
        print("I can't vote")

Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
Ans:
    import functools
    numbers = [12, 75, 150, 180, 145, 525, 50]
    res=0
    s= lambda res, x: res+x
    res=functools.reduce(s,numbers)
    print(res)


Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
Ans:
    values = input("Enter multiple values separated by space: ").split()
    if(values[0]>values[1] and values[0]>values[2]):
            print(values[0])
    elif(values[2]>values[1] and values[2]>values[1]):
            print(values[2])
    else:
        print(values[1])

Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
Ans:
    numbers = [12, 75, 150, 180, 145, 525, 50]
    for i in numbers:
        if(i<=500):
            if(i%5==0 and i<150):
                print(i)
        else:
            break

Q26. What is a string? How can we declare string in Python?
Ans: In Python, a string is a sequence of characters enclosed within either single quotes (') or double quotes ("). Strings are immutable, meaning once they are created, their contents cannot be changed.
mystr = 'Hi'

Q27. How can we access the string using its index?
Ans: you can access a specific character in a string by referring to its index position within square brackets []
Ex: mystr = 'Hi'
    first_char=mystr[0]
Q28. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "iNeuron"
```
Ans: 
    string = "Big Data iNeuron"
    print(string.split(" ")[2])
Q29. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "norueNi"
```
Ans:
    string = "Big Data iNeuron"
    s=string.split(" ")[2]
    print(s[::-1])
Q30. Resverse the string given in the above question.
Ans: print(string[::-1])
Q31. How can you delete entire string at once?
Ans: del(string)
Q32. What is escape sequence?
Ans: (\) Used to consider " or ' in the string.
Q33. How can you print the below string?
```
'iNeuron's Big Data Course'
```
Ans: s='iNeuron\'s Big Data Course'

Q34. What is a list in Python?
Ans: Used to store multiple heterogenous data in same variable.

Q35. How can you create a list in Python?
Ans: l=[]

Q36. How can we access the elements in a list?
Ans: Using indexing

Q37. Write a code to access the word "iNeuron" from the given list.
```
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
``` 
Ans: lst[4][2]

Q38. Take a list as an input from the user and find the length of the list.
Ans: values = input("Enter multiple values separated by space: ").split()
     print(len(values))

Q39. Add the word "Big" in the 3rd index of the given list.
```
lst = ["Welcome", "to", "Data", "course"]
```
Ans: lst.insert(2,"Big")

Q40. What is a tuple? How is it different from list?
Ans: Used to store multiple heterogenous data in same variable. Tuple is immutable.

Q41. How can you create a tuple in Python?
Ans: x=(1,2,3)

Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.
Ans: No, can't. Tuple is immutable

Q43. Can two tuple be appended. If yes, write a code for it. If not, why?
Ans: tuple1+tuple2

Q44. Take a tuple as an input and print the count of elements in it.
Ans: 
    string = tuple(input().split(" "))
    print(len(string))
Q45. What are sets in Python?
Ans: A set is an unordered collection of unique elements.

Q46. How can you create a set?
Ans: you can create a set using curly braces {} or the set() constructor.
m = {1, 2, 3, 4}

Q47. Create a set and add "iNeuron" in your set.
Ans:
    m={"asd","asdf"}
    m.add("iNeuron")
    print(m)

Q48. Try to add multiple values using add() function.
Ans:
    s.add(1)
    s.add(2)

Q49. How is update() different from add()?
Ans: add() adds a single element to the set, while update() can add multiple elements from an iterable to the set

Q50. What is clear() in sets?
ANs: Empty a set

Q51. What is frozen set?
Ans: Frozenset is an immutable version of a set.

Q52. How is frozen set different from set?
Ans: Frozenset is an immutable, set is an mutable

Q53. What is union() in sets? Explain via code.
Ans: Include all unique values in both sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}
result_set = set1.union(set2, set3)
print(result_set)  # Output: {1, 2, 3, 4, 5, 6, 7}

Q54. What is intersection() in sets? Explain via code.
Ans: Include only common values in both sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
set3 = {4, 5, 6}
result_set = set1.intersection(set2, set3)
print(result_set)  # Output: {4}

Q55. What is dictionary in Python?
Ans: Dictionary is a mutable and unordered collection of key-value pairs.

Q56. How is dictionary different from all other data structures.
Ans: Accesing element is via keys instead of indexing

Q57. How can we delare a dictionary in Python?
Ans: x={"one":1,""two":2}

Q58. What will the output of the following?
```
var = {}
print(type(var))
```
Ans: dict

Q59. How can we add an element in a dictionary?
Ans: 
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3 //add

Q60. Create a dictionary and access all the values in that dictionary.
Ans:
    my_dict = {
        'name': 'Alice',
        'age': 25,
        'city': 'London',
        'country': 'UK'
    }
    values = list(my_dict.values())
    print(values)

Q61. Create a nested dictionary and access all the element in the inner dictionary.
Ans:
my_dict = {
    'outer_key1': {
        'inner_key1': 'value1',
        'inner_key2': 'value2'
    },
    'outer_key2': {
        'inner_key3': 'value3',
        'inner_key4': 'value4'
    }
}
inner_dict_values = my_dict['outer_key1']
print(inner_dict_values)
value1 = my_dict['outer_key1']['inner_key1']
value2 = my_dict['outer_key1']['inner_key2']
print(value1, value2)

Q62. What is the use of get() function?
Ans:The get() method in Python dictionaries is used to retrieve the value associated with a given key

Q63. What is the use of items() function?
Ans: The items() method in Python dictionaries returns a view object that displays a list of key-value tuple pairs

Q64. What is the use of pop() function?
Ans: Removes and returns the value for a specified key.

Q65. What is the use of popitems() function?
Ans: Removes and returns the last inserted key-value 

Q66. What is the use of keys() function?
Ans: list of all the keys in the dictionary

Q67. What is the use of values() function?
Ans:  list of all the values in the dictionary

Q68. What are loops in Python?
Ans: loops are control structures used to execute a block of code repeatedly wrt conditions.

Q69. How many type of loop are there in Python?
Ans: for, while

Q70. What is the difference between for and while loops?
Ans: for loop iterates through a sequence or an iterable object for a specified number of times.
while loop continues iterating as long as a given condition is true

Q71. What is the use of continue statement?
Ans: continue statement in Python is used to skip the rest of the code inside a loop.

Q72. What is the use of break statement?
Ans: exit or terminate a loop

Q73. What is the use of pass statement?
Ans: does nothing and allows the code to proceed without any errors

Q74. What is the use of range() function?
Ans: generates a sequence of numbers

Q75. How can you loop over a dictionary?
Ans: 
    for key, value in my_dict.items():
        print(key, value)

### Coding problems
Q76. Write a Python program to find the factorial of a given number.
Ans:
def fact(n):
    if(n==1):
        return n
    elif(n>1):
        return n*(fact(n-1))
    elif(n==0):
        return 0
    else:
        return ("not possible")

print(fact(-3))

Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (P*R*T)/100
Ans:
def simple_intrest(p,r,t):
    return ((p*r*t)/100)
print(simple_intrest(100, 2, 3))

Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.
Ans:
def compound_intrest(p,r,t):
    return (p*((1+(r/100))**t))
print(compound_intrest(100, 2, 3))

Q79. Write a Python program to check if a number is prime or not.
Ans:
def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

num = 10

if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

Q80. Write a Python program to check Armstrong Number.
Ans:
def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == num

number = int(input("Enter a number: "))

if is_armstrong(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")

Q81. Write a Python program to find the n-th Fibonacci Number.
Ans:
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

num = int(input("Enter a number: "))
result = fibonacci(num)
print(f"The {num}-th Fibonacci number is: {result}")

Q82. Write a Python program to interchange the first and last element in a list.
Ans:
def interchange(l):
    l[0], l[-1] = l[-1], l[0]
    return l

result = interchange([1, 2, 3, 4, 5])
print(result)

Q83. Write a Python program to swap two elements in a list.

Q84. Write a Python program to find N largest element from a list.

Q85. Write a Python program to find cumulative sum of a list.

Q86. Write a Python program to check if a string is palindrome or not.

Q87. Write a Python program to remove i'th element from a string.

Q88. Write a Python program to check if a substring is present in a given string.

Q89. Write a Python program to find words which are greater than given length k.

Q90. Write a Python program to extract unquire dictionary values.

Q91. Write a Python program to merge two dictionary.

Q92. Write a Python program to convert a list of tuples into dictionary.
```
Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
```

Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
```
Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]
```

Q94. Write a Python program to get all combinations of 2 tuples.
```
Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
```

Q95. Write a Python program to sort a list of tuples by second item.
```
Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
```

Q96. Write a python program to print below pattern.
```
* 
* * 
* * * 
* * * * 
* * * * * 
```
Q97. Write a python program to print below pattern.
```
    *
   **
  ***
 ****
*****
```

Q98. Write a python program to print below pattern.
```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```

Q99. Write a python program to print below pattern.
```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
```

Q100. Write a python program to print below pattern.
```
A 
B B 
C C C 
D D D D 
E E E E E 
```
