

# class Edureka():
#     a=45
#     @classmethod
#     def myCustomerConstructor(cls, employee_strength):
#         cls.employee_strength = employee_strength
#         return cls.employee_strength
        
# obj1 = Edureka();
# obj = Edureka.myCustomerConstructor(400)
# print(obj1.a)
# print(obj)

# Inheritance
# class base1:
#     def func(self):
#         print("In Class base1")

# class sub(base1):
#     pass

# obj = sub()
# obj.func()

# multiple inheritance
# class First(object):
#     def __init__(self):
#         super(First,self).__init__()
#         print('first')

# class Second(object):
#     def __init__(self):
#         super(Second,self).__init__()
#         print('second')
        
        
# class Third(Second, First):
#     def __init__(self):
#         super(Third,self).__init__()
#         print('third')

# Third()


# Multilevel inheritance
# class Animal:
#     def eat(self):
#         print("Eating..")

# class Dog(Animal):
#     def bark(self):
#         print("Barking...")

# class BabyDog(Dog):
#     def weep(self):
#         print("Weeping...")
        
# d = BabyDog()
# d.eat()
# d.bark()
# d.weep()

# class Parent:
#     def myMethod(self):
#         print("Calling parent method")

# class Child(Parent):
#     def myMethod(self):
#        print("Calling child method")
       
# c = Child()
# c.myMethod()


# class Rectangle():
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
        
#     def getArea(self):
#         print(self.length * self.breadth," is area of rectangle")

# class Square(Rectangle):
#     def __init__(self, side):
#         self.side = side
#         Rectangle.__init__(self,side,side)
#     def getArea(self):
#         print(self.side * self.side," is area of square")
        
# s = Square(4)
# r = Rectangle(2,4)
# s.getArea()
# r.getArea()



class Edureka:
    def __init__(self,courseName):
        self.courseName = courseName

    def setCourseName(self, courseName):
        self.courseName = courseName.upper()

    def getCourseName(self):
        return self.courseName
    
obj = Edureka("Python")

print(obj.getCourseName())

obj.setCourseName("Data Science")
print(obj.getCourseName())