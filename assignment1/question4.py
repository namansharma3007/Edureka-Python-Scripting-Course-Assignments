# Question 4

# from curses.ascii import isdigit


my_str = input("Enter the input string:\n")

digits=letters=0

for c in my_str:
    if c.isalpha():
        letters+=1
    else:
        digits+=1

print("Letters: ",letters)
print("Digits: ",digits)