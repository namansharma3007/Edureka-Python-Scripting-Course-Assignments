def func():
    print("func() in one.py")

print("Top-level in one.py")

if __name__ == "__main__":
    print("one.py in being run directly")
else:
    print("one.py is being imported ino another module")
