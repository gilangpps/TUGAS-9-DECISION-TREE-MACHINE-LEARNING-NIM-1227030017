# -*- coding: utf-8 -*-
"""MATERI 9-DECISION TREE MACHINE LEARNING-1227030017.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13ttFtYGF8lJKQfQjpcSCDG900SuSDPCt
"""

from sklearn import tree

#Database: Gerbang logika AND
# x = data; y = target

x = [[0,0],[0,1],[1,0],[1,1]]
y = [0,0,0,1]

#Training and Clasiy

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

#Prediction
print("Logika AND Metode Decision Tree")
print("0 dan 0 = ", clf.predict([[0,0]]))
print("0 dan 1 = ", clf.predict([[0,1]]))
print("1 dan 0 = ", clf.predict([[1,0]]))
print("1 dan 1 = ", clf.predict([[1,1]]))

#Kode Program Prediksi Data

from google.colab import drive
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

#Cantolkan ke Drive
drive.mount('/content/drive')

#Path ke Berkas dari Google Drive
FileDB = '/content/drive/My Drive/DATASET DECISION TREE/Sinus.txt' #Sesuaikan path file
Database = pd.read_csv(FileDB, sep=",", header=0)

#Lihat data
print("--------------------")
print(Database)
print("--------------------")

#Menentukan Figur dan Target

#x data, y target
x = Database[['Feature']]
y = Database.Target

#Membuat dan Melatih Model

reg = DecisionTreeRegressor(random_state=1)
reg = reg.fit(x,y)

# Display predicted data
xx = np.arange(1, 21, 1)
n = len(xx)
print("xx(i) Decision Tree")
for i in range(n):
  y_dct = reg.predict([[xx[i]]])
  print('{:.2f}'.format(xx[i]), y_dct)
# Plot the predicted data
y_dct2 = reg.predict(x)
plt.figure()

plt.plot(x, y_dct2, color='red')
plt.scatter(x, y, color='blue')
plt.title('Predisksi Data Menggunakan Decision Tree')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Decision Tree', 'data'], loc=2)
plt.show()