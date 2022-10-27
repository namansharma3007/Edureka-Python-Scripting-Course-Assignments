import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from os import environ


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == "__main__":
    suppress_qt_warnings()


dataset = pd.read_csv("C:/Users/naman/Desktop/Edureka Python/assignment5/BigMartSalesData.csv")

data = dataset.copy()

data = data.drop(data[data.Year!=2011].index)

print(data.to_string())

total = data.groupby('Month').agg({'Amount':np.sum})
print (total)
data.groupby('Month').agg({'Amount':np.sum}).plot(kind='line', color='red')
plt.xlabel('Year of 2011')
plt.ylabel('Total Sales')
plt.title('Sales per month')
plt.show()


data.groupby('Month').agg({'Amount':np.sum}).plot(kind='bar', color='orange')
plt.xlabel('Year of 2011')
plt.ylabel('Total Sales')
plt.title('Sales Per Month in 2011')
plt.show()


plt.figure(figsize=(10,10))
sales_country = data.groupby('Country').agg({'Amount':np.sum})
sales_country = sales_country.to_dict()['Amount']


dataValues = list(sales_country.values())
labelValues = list(sales_country.keys())



plt.pie(dataValues, labels=labelValues,autopct='%1.1f%%')  # type: ignore
plt.show()


sales_invoice = dataset.groupby('InvoiceNo').agg({'Amount':np.sum})
print(sales_invoice)
plt.scatter(sales_invoice.values,sales_invoice.values,color='magenta')
plt.grid(True)
plt.show()