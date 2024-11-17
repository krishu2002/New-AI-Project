# Module Buiding
# linear Regression
# Calling DATA
from data import df,X_test,X_train,Y_test,Y_train
# calling class
from sklearn.linear_model import LinearRegression
# Making module
lr = LinearRegression()
lr.fit(X_train,Y_train)