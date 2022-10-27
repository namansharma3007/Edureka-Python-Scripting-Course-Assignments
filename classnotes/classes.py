# class Demo:
#     """
#     Explaining a class
#     """
#     count = 0

# print("Demo.__dict__",Demo.__dict__)
# print("Demo.__doc__",Demo.__doc__)
# print("Demo.__name__",Demo.__name__)
# print("Demo.__module__",Demo.__module__)
# print("Demo._basest__",Demo.__bases__)


# class Edureka():
#     def __init__(self):
#         self.__pri = ("I am Private")
#         self._pro = ("I am Protected")
#         self.pub = ("I am public")
        
#     def __del__(self):
#         self._pro = None
#         print("Objject will be deleted")

#     def __privateMethod(self):
#         print("I am a private method")

# obj = Edureka();
# print(obj.pub)
# print(obj._pro)
# # print(obj.__pri) # cannot be accessed

# obj._Edureka__privateMethod()  # if we wish to call private method this is the syntax we need to apend the name of class and '_' as  a prefix

# print(obj._Edureka__pri)


