import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = "C:/Users/naman/Desktop/Edureka Python/assignment5/{name}"


# Question no 1

hurricanesPath = path.format(name="Hurricanes.csv")

data_hurricanes = pd.read_csv(hurricanesPath)

x = data_hurricanes['Year']
y = data_hurricanes['Hurricanes']

plt.bar(x,y)
plt.xlabel("Year")
plt.ylabel("Hurrianes")
plt.grid()
plt.title('Hurricanes vs Year')
plt.show()


# Question no 2

city_temples_path = path.format(name="CityTemps.csv")

data_city_temples = pd.read_csv(city_temples_path)

x_moscow = data_city_temples['Moscow']
x_sanfrancisco = data_city_temples['San Francisco']

plt.hist(x_moscow,len(x_moscow))
plt.hist(x_sanfrancisco,len(x_moscow))

plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.title("Temperature of Moscow and San Framcisco")

plt.show()

# Question no 3


cars_data_path = path.format(name="Cars2015.csv")
cars_data = pd.read_csv(cars_data_path)

# Drop teh columns which are not required
cars_data = cars_data.drop(['Model','Type','LowPrice','HighPrice','Drive','CityMPG','HwyMPG','FuelCap','Length'], axis=1)

cars_data = cars_data.drop(['Width','Wheelbase','Height','UTurn','Weight','Acc030','Acc060'],axis=1)

cars_data = cars_data.drop(['QtrMile','PageNum','Size'],axis=1)

cars_data = cars_data['Make'].value_counts()



carNames = []
dataValues = []

for x in cars_data.items():
    carNames.append(x[0])
    dataValues.append(x[1])

    
plt.figure(figsize=(50,8))
plt.title("Car Releases")

plt.pie(dataValues,labels=carNames,autopct='%.1f%%',radius=1.1)  # type: ignore
plt.rcParams.update({'font.size':10})

plt.show()


# Question no 4

df_data_file = pd.read_csv(path.format(name="data_file.txt"))
df_data_file.to_csv(path.format(name="data_file.csv"))

# Question no 5

# 5.1
X = [1, 2, 3, 4]
Y = [20, 21, 20.5, 20.8]

plt.plot(X, Y)
plt.show()

# 5.2

plt.plot(X, Y)
plt.grid()
plt.show()


# 5.3

plt.setp(plt.gca().get_xticklabels(), rotation=90,horizontalalignment='right')

# 5.4

plt.plot(X, Y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# 5.5

y_error = [0.12, 0.13, 0.2, 0.1]

plt.plot(X, Y, y_error)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# 5.6

plt.figure(figsize=(3, 4))

# 5.7

plt.rcParams.update({'font.size': 14})

# 5.8

x = np.random.random(50)
y = np.random.random(50)

plt.scatter(x, y)
plt.show()

# 5.9

df = pd.DataFrame({
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
    'female': [0, 1, 1, 0, 1],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70]
})

plt.scatter(df["preTestScore"], df["postTestScore"])
plt.xlabel("preTestScore")
plt.ylabel("postTestScore")
plt.title("preTestScore vs postTestScore")
plt.legend(["preTestScore", "postTestScore"])
plt.show()


# Questino no 10

df = pd.DataFrame({
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
    'female': [0, 1, 1, 0, 1],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70]
})

x = df["preTestScore"]
y = df["postTestScore"]
colors = df["female"]


plt.scatter(x, y, c=colors, alpha=0.5)
plt.xlabel("preTestScore")
plt.ylabel("postTestScore")
plt.title("preTestScore vs postTestScore")
plt.legend(["preTestScore", "postTestScore"])
plt.show()