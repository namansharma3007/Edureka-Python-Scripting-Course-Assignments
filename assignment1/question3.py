# Question 3

no = int(input("Enter the no:\n"))

#  Function to check even digits
def checkEvenNo(no):
    result=[]

    while(no != 0):
        remainder = no%10;
        if remainder%2 == 0:
            result.append(remainder)
        no //= 10

    return result


if no >=1000 and no<=3000:
    print(checkEvenNo(no))

else:
    print("Please enter no between 1000 and 3000 inclusive")


