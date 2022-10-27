import one

print("top level in two.py")
one.func()

if __name__ == "_main__":
    print("two.py is run directly")
else:
    print("two.py is being run directly")