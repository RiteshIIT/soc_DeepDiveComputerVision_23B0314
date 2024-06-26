import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv("Linear Regression - Sheet1.csv")
# plt.scatter(data.X,data.Y,color='blue')
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()


msk=np.random.rand(len(data))<0.8
train=data[msk]
test=data[~msk]

regr=linear_model.LinearRegression()
train_x=np.asanyarray(train[['X']])
train_y=np.asanyarray(train[['Y']])
regr.fit(train_x,train_y)

print("Weight : ",regr.coef_)
print("Bias :", regr.intercept_)

test_x=np.asanyarray(test[['X']])
test_y=np.asanyarray(test[['Y']])
test_y_=regr.predict(test_x)

print("R2 score is ", r2_score(test_y,test_y_))

plt.scatter(train.X,train.Y,color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x+regr.intercept_[0],'-r')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

