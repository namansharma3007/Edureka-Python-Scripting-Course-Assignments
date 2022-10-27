# Question 1
import math
from math import radians, sin, cos, acos

x,y = 0, 0

while True:
    step = input("Type in UP/DOWN/LEFT/RIGHT #step number: ")

    if step == "":
        break

    else:
        step = step.split(" ")

        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])

c = math.sqrt(x**2 + y**2)

print("Distance:", c)


# Question 2

string = input("Enter list of items (comma seperated)>>> ")
find_ele = input("Enter the elements which needs to find>>> ")

list_eles = str(string).split(",")

if find_ele in list_eles:
    print(f"{find_ele} is present in given list at position {list_eles.index(find_ele)+1}")
else:
    print(f"{find_ele} is not present in given list")
    
# Question 3

from datetime import datetime


def get_part_of_day(hour):
    return (
        "light" if 5 <= hour <= 18
        else
        "dark"
    )


h = datetime.now().hour

print(f"Its {get_part_of_day(h)}  right now.")

# Question no 4


print("Input coordinates of two points:")
slat = radians(float(input("Starting latitude: ")))
slon = radians(float(input("Ending longitude: ")))
elat = radians(float(input("Starting latitude: ")))
elon = radians(float(input("Ending longitude: ")))

dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
print("The distance is %.2fkm." % dist)


#Question no 5
# Done on another sheet

#Question no 6
import math 
 
lower = math.ceil(2000 / 7) 
upper = math.floor(3201 / 7) 
for i in range(lower, upper+1): 
    if (7 * i) % 5 != 0: 
        print(7 * i, end =' ') 
    else: 
        continue
    
    
# Question no 7

def factorial(n):
    if n < 2:
        return n
    
    return (n) * factorial(n-1);

input_No = int(input("Enter the no to find its factorial: "))
print(f"{factorial(input_No)} is the factorial of {str(input_No)}")

# Question no 8

numbers = input("Provide D: ")
numbers = numbers.split(',')

result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result_list.append(Q)

print(result_list)


# Question no 9
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)


# Question no 10

phrase = input("Input words: ")

phrase_list = phrase.split(",")
phrase_list.sort()
print((', ').join(phrase_list))

#  Question no 11
lines = []
while True:
    l = input("Please enter line: ")
    if l:
        lines.append(l.upper())
    else:
        break;

for l in lines:
    print(l)
    
    
#Question no 12
    
phrase = input("Type in: ")
phrase_splited = phrase.split(' ')

word_list = []
for i in phrase_splited:
    if i not in word_list:
        word_list.append(i)
    else:
        continue
word_list.sort()
print((' ').join(word_list))

# Question no 13
items = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)
    if not x%5:
        items.append(p)
print(','.join(items))


# Question no 14
phrase = input("Type in: ")
phrase = list(phrase)

u, l = 0, 0
for i in phrase:
    if i.isupper():
        u = u + 1
    if i.islower():
        l = l + 1
    else:
        pass

print("UPPER:", u)
print("lower:", l)

# Question no 15


arr = [1,2,3,4]
print(math.fsum(arr))

print(math.sum(arr))