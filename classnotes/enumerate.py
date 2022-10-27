grocery = ["apples","banana","papaya"]
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

print(list(enumerateGrocery))

enumerateGrocery = enumerate(grocery,10)
print(list(enumerateGrocery))