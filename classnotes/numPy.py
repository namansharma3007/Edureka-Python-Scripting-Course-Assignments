import numpy as np


# a = np.array([1,2,3]) # [1 2 3]  with no commas
# b = np.array([[1,2,3],[4,5,6]])
# # [[1 2 3]
# #  [4 5 6]]
# c = np.array([[1,2,9,3],[4,5,6]])
# # [list([1, 2, 9, 3]) list([4, 5, 6])]
# print(b)
# print(c)

# a = np.arange(1,100)
# b = np.zeros((5,3))
# print(b)

# vector = np.linspace(0, 20, 5)
# print(vector)


# a = np.zeros(8)

# print(a)

# a = a.reshape((2,2,2))
# print(a)
# print(a.ravel())

# arr = np.arange(20)

# element = arr[6]
# print(element)
# print(type(element))
# print(type(element+7))

# arr_slice = slice(1,10,3)

# print(arr[:20:2])


# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# print(arr[0:2,0:1])
# print(arr.shape)

# print(arr.ndim)

# print(arr.itemsize)

# arr = np.empty([3,2],dtype=float)

# print(arr)

# arr = np.arange(20)

# arr2 = np.array([[1,2,3],[4,5,6]])

# print(arr2)

# np.savetxt('test.txt',arr2)

# new_arr = np.loadtxt('test.txt')

# print(new_arr)

arr2 = np.array([[1,2,3],[4,5,6]])

# print(arr2)

np.savetxt('test.csv',arr2, delimiter=",")

arr = np.genfromtxt('test.csv', delimiter=",")

print(arr)