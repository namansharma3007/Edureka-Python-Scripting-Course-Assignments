from cProfile import label
from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == "__main__":
    suppress_qt_warnings()

import matplotlib.pyplot as plt
import numpy

# y_values = [1,2,3,4,5,10]
# X = numpy.arange(0,5,0.01)
# X2 = range(5)

# # plt.plot(X2,[i**2 for i in X2])
# # plt.plot(X2,[i**10 for i in X2])

# plt.plot(X2,[i*i for i in X2],label="linear")
# plt.plot(X2,[i*i*i for i in X2],label="square")
# plt.plot(X2,[i**4 for i in X2],label="raised to the power of 4")
# plt.grid(True)
# plt.legend()
# # plt.axis([1,3,1,3])

# # plt.xlim(1,3)
# # plt.ylim(1,3)

# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.title("Learning matplotlib")
# plt.savefig('myplot.png')
# plt.show()


# y= numpy.random.randn(10,10)

# plt.hist(y,100)
# plt.show()

# plt.bar([1.5,2.6,4.8],[40,55,85])
# plt.show()

# d = {'a':25,'b':45,'c':52}

# for i,key in enumerate(d):
#     plt.bar(i,d[key])
    
# plt.xticks([0,1,2],d.keys())  # type: ignore
    
# plt.show()


# plt.figure(figsize=(8,6))

# plt.pie([40,25,5,100],labels=["Python","Java","Java Script","machine Learning"])

# plt.show()


# x = numpy.random.rand(10)
# y = numpy.random.randn(10)
# plt.scatter(x,y)
# plt.show()


y = numpy.arange(1,10)

plt.plot(y,'o')
plt.plot(y**2, 'D')
plt.plot(y**3, '^')
plt.grid()
plt.show()