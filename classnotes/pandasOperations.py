import pandas
import numpy

# arr = numpy.array([8,9,5,66,47,63,5461,654])

# data_dict = {'a':1,'b':2,'c':3,'d':5465,'e':952}

# series = pandas.Series(data_dict)
# series2 = pandas.Series(arr)

# print(series[2:])


# listx = [10,20,30,40,50]

# list2 = [{'a':1,'b':3},{'a':4,'b':5},{'a':7,'b':9,'c':85,'d':97461}]

# table = pandas.DataFrame(list2,index=['row-1','row-2','row-3'])

# print(table)

# list2 = [{'a':1,'b':3},{'a':4,'b':5},{'a':7,'b':9,'c':85,'d':97461}]

# subjects = ['Maths','Physics','Chemistry']

series1 = pandas.Series([40,50,60],index=['Maths','Physics','Chemistry'])
series2 = pandas.Series([45,70,90,92],index=['Maths','Physics','Chemistry','Java'])

table = pandas.DataFrame({
    "Tom":series1,
    "Jerry":series2
})
table["Stuart"] = pandas.DataFrame([85,69,52,79,96],index=['Maths','Physics','Chemistry','Java','English'])

# # del(table['Tom'])  # if you want to print the data that  is deleted follow this convention

# # tom_series = table.pop('Tom') # will return the data removed
# # print(tom_series)
# # print(table)

# # print(table.loc['Maths'])

# # print(table.iloc[0])
# # print(table.iloc[1])
# # print(table.iloc[2])


table = table.append(pandas.DataFrame([[95,65,74]],columns=['Tom','Jerry','Stuart']))

# # print(table)

# table = table.drop("Java")

# print(table)

# table = pandas.read_csv('pandas_data.csv')

table.to_csv('pandas_data.csv')

# print(table)