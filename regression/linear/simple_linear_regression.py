# -*- coding: utf-8 -*-
"""Copy of simple_linear_regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EkDKvkPdK9vPzRieKEqJr2-gyrEFpKsh

# Simple Linear Regression

## Importing the libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""## Importing the dataset"""

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2 , random_state = 0 )

"""## Training the Simple Linear Regression model on the Training set"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

"""## Predicting the Test set results"""

y_predicted = regressor.predict(X_test)

"""## Visualising the Training set results"""

plt.scatter(X_train,y_train , color = 'red')
plt.plot(X_train , regressor.predict(X_train), color = 'blue')
plt.title('Salary Vs year of experience (Training set)')
plt.xlabel('years of experience')
plt.ylabel('Salary')
plt.show()

"""## Visualising the Test set results"""

plt.scatter(X_test ,y_test , color = 'red')
plt.plot(X_test , regressor.predict(X_test) , color = 'blue')
plt.title('Salary Vs year of experience ( Test set ) ')
plt.xlabel('years of experience')
plt.ylabel('Salary')
plt.show()