import re
import random

# Question 1

nums = set([1,1,2,3,3,3,4,4])
print(len(nums)) # 4


# Question no 2

d = {"john":40,"peter":45}
print(list(d.keys())) #['john', 'peter']

# Question no 3


password = input("Enter password:\n")

x = True

while(x):
    if len(password) < 6 or len(password) > 12:
        break
    elif not re.search("[a-z]",password):
        break
    elif not re.search("[0-9]",password):
        break
    elif not re.search("[A-Z]",password):
        break
    elif not re.search("[$#@]",password):
        break
    else:
        print("Valid Password")
        x = False
        break

if x:
    print("Not a Valid Password")
    
# Question 4

a=[4,7,3,2,5,9]
for i in range(len(a)):
    print("index:",i,"=",a[i])
    
    # index: 0 = 4
    # index: 1 = 7
    # index: 2 = 3
    # index: 3 = 2
    # index: 4 = 5
    # index: 5 = 9

# question no 5

input_str = input("Enter the string:\n")

for element in input_str[::2]:
    print(element,end='') #Helloworld


# Question no 6
firstString = input("enter the string to be reversed:\n")

print(firstString[::-1])


# Question no 7

strInput = input("Enter the string to check the no ocurence of each alphabet:\n")

answer = {}

for element in strInput:
    if element in answer.keys():
        answer[element]+=+1
    else:
        answer[element]=1

for element in answer:
    print(element+","+str(answer[element]))

# a,2
# b,2
# c,2
# d,1
# e,1
# f,1
# g,1

# Question no 8

list1={1,3,6,78,35,55}

list2={12,24,35,24,88,120,155}

print(list1 & list2)


# Question no 9

arrList = [12,24,35,24,88,120,155,88,120,155]

print(set(arrList))

# Question no 10

arrList1 = [12,24,35,24,88,120,155]


for element in arrList1:
    if element == 24:
        arrList1.remove(element)

print(arrList1)

# Question no 11

arrList2 = [12,24,35,70,88,120,155]

arrList2 = [x for (i,x) in enumerate(arrList2) if i not in (0,4,5) ]

print(arrList2) #[24, 35, 70, 155]

# Question no 12

arrList3 = [12,24,35,70,88,120,155]

arrList3 = [x for x in arrList3 if x%5!=0 and x%7 !=0]

print(arrList3)

# question no 13

resultArr = []

flag = True
while(flag):
    randomNo = random.choice([i for i in range(1,1001) if i%5==0 and i%7==0])
    if randomNo not in resultArr:
        resultArr.append(randomNo)
        if len(resultArr) == 5:
            flag = False
            break

print(resultArr) #[280, 420, 35, 945, 805]

# Question no 14
inputRange = int(input("Enter the no:\n"))
sum=0;
for i in range(1,inputRange+1):
    print(i)
    sum+=(i/(i+1))

print('%.2f' % sum) # 3.55
