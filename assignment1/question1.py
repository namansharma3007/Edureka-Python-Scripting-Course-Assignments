# Questino no 1
no = int(input("Enter the no: \n"))

factors = []
oddEven={"odd":[],"even":[]}

for i in range(1,no+1):
    if no%i == 0:
        if i%2 == 0:
            factors.append(i)
            oddEven["even"].append(i)
        else:
            factors.append(i)
            oddEven["odd"].append(i)

print(factors)
print(oddEven)  