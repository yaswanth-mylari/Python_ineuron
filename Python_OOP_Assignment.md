## Python OOP Assignment
Q1. What is the purpose of Python's OOP?
Ans: OOPs is to organize code into reusable and efficient structures.
    a. Class
    b. Object
    c. Abstraction
    d. Polymorphism
    e. Encapsulation
    f. Inheritence

Q2. Where does an inheritance search look for an attribute?
Ans: First with in instance, next with in class, finally in parent class

Q3. How do you distinguish between a class object and an instance object?
Ans:  Class object is the blueprint or template, but instance object is kind of a variable for the class which has all the attributes/features.
Ex: class MyClass: //class object
    inst_object=MyClass()//instance object

Q4. What makes the first argument in a class’s method function special?
Ans: First argument in a class’s method function is self. Self is used to refer to current instance of the object. we no need to pass that argument as it goes as current object reference.

Q5. What is the purpose of the init method?
Ans: init is a constructor. As soon as object is created this will trigger and perform actions as part of that function.

Q6. What is the process for creating a class instance?
Ans: create class, define attributes in it. create an instance object
    class MyClass:
        def __init__(self, arg1, arg2):
            self.attribute1 = arg1
            self.attribute2 = arg2
    obj = MyClass(value1, value2)

Q7. What is the process for creating a class?
Ans: Create a class and define its behavior, attributes, and methods. Instances can then be created from this class.
    class MyClass:
        def __init__(self, arg1, arg2):
            self.attribute1 = arg1
            self.attribute2 = arg2

Q8. How would you define the superclasses of a class?
Ans: Superclass refers to the class from which another class inherits. To define the superclass of a class, you can use inheritance, specifying the superclass in the class definition.
class parent:
    def __init__(self, value):
        self.value = value
class child(parent):
    def __init__(self, value, value1):
        super().__init__(value)
        self.value1 = value1

Q9. What is the relationship between classes and modules?
Ans: Classes: Classes are blueprints for creating objects.
     Modules: Modules are files containing Python definitions, statements, functions, and classes. 

Q10. How do you make instances and classes?
Ans:
    class MyClass:  //class
        def __init__(self, arg1, arg2):
            self.attribute1 = arg1
            self.attribute2 = arg2
    obj = MyClass(value1, value2) //object instance

Q11. Where and how should be class attributes created?
Ans: Class attributes in Python are created within the class definition but outside of any class methods.
     class MyClass:
        class_attr="Class attribute"
        def __init__(self, arg1, arg2):
            self.attribute1 = arg1
            self.attribute2 = arg2

Q12. Where and how are instance attributes created?
Ans:Class attributes in Python are created within the class definition, inside of any class methods.
     class MyClass:
        class_attr="Class attribute"
        def __init__(self, arg1, arg2):
            self.attribute1 = arg1// instance attribute
            self.attribute2 = arg2

Q13. What does the term "self" in a Python class mean?
Ans:Self is used to refer to current instance of the object. we no need to pass that argument as it goes as current object reference.

Q14. How does a Python class handle operator overloading?
Ans: operator overloading allows classes to define or redefine the behavior of built-in operators for their instances. 

Q15. When do you consider allowing operator overloading of your classes?
Ans: Operator overloading in Python can be useful when you want your custom objects to mimic the behavior of built-in types

Q16. What is the most popular form of operator overloading?
Ans:  Most common form of operator overloading typically involves arithmetic operators like +, -, *, /, and comparison operators like ==, !=, <, >, etc. Overloading these operators allows programmers to define custom behaviors for objects of user-defined classes.

Q17. What are the two most important concepts to grasp in order to comprehend Python OOP code?
Ans: Classes and Objects

Q18. Describe three applications for exception processing.
Ans: File not found Exception
     Divisible by  zero exception
     Index out of bound exception

Q19. What happens if you don't do something extra to treat an exception?
Ans: Program will halt when exception raises

Q20. What are your options for recovering from an exception in your script?
Ans: Handling them with try-except block

Q21. Describe two methods for triggering exceptions in your script.
Ans: def method1():
        l=[1,2]
        print(l[3])
     def method2():
        x=3/0

Q22. Identify two methods for specifying actions to be executed at termination time, regardless of  
whether or not an exception exists.
Ans: Use finally block.

Q23. What is the purpose of the try statement?
Ans: This will try to execute block of code and if exception raises then control is transferred to except block.

Q24. What are the two most popular try statement variations?
Ans: Try-except
     Try-finally

Q25. What is the purpose of the raise statement?
Ans: Raise used to raise an exception by the user/developer.

Q26. What does the assert statement do, and what other statement is it like?
Ans: Evaluates an expression and raises an AssertionError if the expression is false

Q27. What is the purpose of the with/as argument, and what other statement is it like?
Ans:  It's particularly useful when working with resources that need to be explicitly opened and closed, like files etc. It's like try/finally block

Q28. What are *args, **kwargs?
Ans: The *args parameter in a function definition allows you to pass a variable number of positional arguments. It collects these arguments into a tuple within the function.
The **kwargs parameter in a function definition allows you to pass a variable number of keyword arguments. It collects these arguments into a dictionary within the function.

Q29. How can I pass optional or keyword parameters from one function to another?
Ans: We can use *args and **kwargs within the function calls. 

Q30. What are Lambda Functions?
Ans: Simailar to method/function. its like a single line method.

Q31. Explain Inheritance in Python with an example?
Ans: Feature that allows a child class to inherit properties and behaviors from an parent class.
    class Animal:
        def __init__(self, species, sound):
            self.species = species
            self.sound = sound
        def make_sound(self):
            print(f"The {self.species} makes a {self.sound} sound.")
    class Dog(Animal):
        def __init__(self, name):
            super().__init__("Dog", "bark")
            self.name = name
        def wag_tail(self):
            print(f"{self.name} is wagging its tail.")

Q32. Suppose class C inherits from classes A and B as class C(A,B).Classes A and B both have their own versions of method func(). If we call func() from an object of class C, which version gets invoked?
Ans: It picks func() from left most class with in bracket i.e., A

Q33. Which methods/functions do we use to determine the type of instance and inheritance?
Ans: type of instance: isinstance()
     inheritence: issubclass()
Q34.Explain the use of the 'nonlocal' keyword in Python.
Ans: The nonlocal keyword only applies to variables in enclosing scopes, not global variables. If a variable is not found in the local or enclosing scopes, Python will look for it in the global scope.

Q35. What is the global keyword?
Ans: The global keyword is used to declare that a variable inside a function refers to the global scope's variable rather than creating a new local variable with the same name