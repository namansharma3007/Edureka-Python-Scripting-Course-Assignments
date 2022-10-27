items = [1,2,3,4,5]

squared = list(map(lambda x:x**2,items))

# print(squared)


number_list = range(-5,5)
less_than_zero = list(filter(lambda x: x < 0, number_list))

# print(less_than_zero)
from functools import reduce
product = reduce(lambda x,y: x*y, [2,3])

# print(product)


def random_func(a,b,c,d):
    return a**d + c**b

# print(random_func(a=4,b=5,c=3,d=7))


def info(user,*users):
    print("User of python:")
    print(user)
    for i in users:
        print("Users in python2:")
        print(i)

# info("Annie")
# info("Michael","Pramod","Madhur")

def myFunction(arg1,arg2,arg3,*args,**args2):
    print("arg1:",arg1)
    print("arg2:",arg2)
    print("arg3:",arg3)
    print("*args:",args)
    print("**args2:",args2)

myFunction(1,2,3,4,5,6,7,name="Naman",country="India",age=25)