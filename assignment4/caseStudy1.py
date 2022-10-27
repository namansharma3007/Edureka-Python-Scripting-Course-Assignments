from os import environ
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# To supress warnings

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == "__main__":
    suppress_qt_warnings()
    
    
# Question no 1
path = "C:/Users/naman/Desktop/Edureka Python/assignment4/{name}"

path1 = path.format(name = "SalaryGender.csv")
numpy_array = np.genfromtxt(path1,delimiter=',',skip_header=1)

print(numpy_array)

# Question no 2
#  male: 1 and female:0

menCount = 0
womenCount = 0

for row in numpy_array:
    if row[1] == 1 and row[3] == 1:
        menCount+=1
    if row[1] == 0 and row[3] == 1:
        womenCount+=1
        
print("Total no of men with PhD: {count}".format(count=menCount))
print("Total no of men with PhD: {count}".format(count=womenCount))

# Question no 3
csv_data = pd.read_csv(path1)

# Filter columns
age_phd = csv_data.filter(['Age',"PhD"])


# Filter data from rows
new_df = age_phd.drop(age_phd[age_phd['PhD'] == 0].index)
# people_phd = age_phd[(age_phd.PhD == 1)]
print(new_df)


# Question no 4

totalPhdPeople = 0

for rows in numpy_array:
    if rows[3] == 1:
        totalPhdPeople+=1
        
print("Total no pf phd people:", totalPhdPeople)

# Question no 5

arrayOfNos = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])

print(arrayOfNos[arrayOfNos > 5])

# Question no 6

newArr = np.array([np.nan, 1, np.nan, 2, 3, 4, 5])
print(newArr)

print(newArr[~np.isnan(newArr)])

# Question no 7

randomArray = np.empty([10,10],dtype=int)

maxElement = np.amax(randomArray)
minElement = np.amin(randomArray)

print("Maximum element: ", maxElement)
print("Minimum element: ", minElement)

# Question no 8
meanArray = np.empty(30,dtype=int)

print(np.mean(meanArray))

# Question no 9

newArrayRange = np.arange(11)

newArrayRange[3:10] = np.multiply(newArrayRange[3:10],-1)
print(newArrayRange)

# Question no 10

npy_mat1 = np.random.randint(10, size=(3, 3))
npy_sort = np.sort(npy_mat1)
print("Original Numpy Array : \n ", npy_mat1)
print("Sorted Numpy Array : \n ", npy_sort)

#  Question no 12
npy_mat1 = np.random.randint(10, size=(4, 4, 4))
arr_sum = npy_mat1.sum(axis=2)

print(arr_sum)

#  Question non 13
npy_mat2 = np.random.randint(10, size=(4, 4))
arr_sum11 = np.swapaxes(npy_mat2, 0, 1)
print("Original Array : \n", npy_mat2)
print("\nSwapped Array : \n", arr_sum11)

#  Question no 14
npy_mat3 = np.random.randint(10, size=(4, 4))
npy_mat4 = np.matrix.view(npy_mat3)  # type: ignore
print("", npy_mat3, "\n")
print(npy_mat4)

# Question no 15

df_school_data = pd.read_csv(path.format(name = "middle_tn_schools.csv"))

# print(df_school_data.head())
# df_school_data.describe()

# Phase 2

df_grouped_data = df_school_data.groupby('school_rating').describe()
print(df_grouped_data)

# Phase 3

corrmat = df_grouped_data.corr()
print(corrmat)
f, ax = plt.subplots(figsize=(4, 3))
sns.heatmap(corrmat, ax=ax, cmap="YlGnBu", linewidths=0.1) #type: ignore


# Phase 4

plt.scatter(df_school_data["school_rating"], df_school_data["reduced_lunch"])
plt.grid()
plt.xlabel("Rating")
plt.ylabel("Reduced lunch")
plt.title("School rating vs Reduced lunch")
plt.show()