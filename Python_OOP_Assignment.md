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
Ans: 
Q17. What are the two most important concepts to grasp in order to comprehend Python OOP code?

Q18. Describe three applications for exception processing.

Q19. What happens if you don't do something extra to treat an exception?

Q20. What are your options for recovering from an exception in your script?

Q21. Describe two methods for triggering exceptions in your script.

Q22. Identify two methods for specifying actions to be executed at termination time, regardless of  
whether or not an exception exists.

Q23. What is the purpose of the try statement?

Q24. What are the two most popular try statement variations?

Q25. What is the purpose of the raise statement?

Q26. What does the assert statement do, and what other statement is it like?

Q27. What is the purpose of the with/as argument, and what other statement is it like?

Q28. What are *args, **kwargs?

Q29. How can I pass optional or keyword parameters from one function to another?

Q30. What are Lambda Functions?

Q31. Explain Inheritance in Python with an example?

Q32. Suppose class C inherits from classes A and B as class C(A,B).Classes A and B both have their own versions of method func(). If we call func() from an object of 
class C, which version gets invoked?

Q33. Which methods/functions do we use to determine the type of instance and inheritance?

Q34.Explain the use of the 'nonlocal' keyword in Python.

Q35. What is the global keyword?
