# Calling DATA
from data import df,X_test,X_train,Y_test,Y_train
# calling class
from building import lr
# TESTING module
Y_lr_train_pred = lr.predict(X_train)
Y_lr_test_pred = lr.predict(X_test)
# Printing Results
# print(Y_lr_train_pred)        ---===>
# print(Y_lr_test_pred)         ---===>