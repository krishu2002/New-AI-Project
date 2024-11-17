import matplotlib.pyplot as plt
import numpy as np
from Module import Y_lr_test_pred,Y_lr_train_pred
from data import df,X_test,X_train,Y_test,Y_train
from building import lr
plt.figure(figsize=(5,5))
plt.scatter(x = Y_train , y = Y_lr_train_pred, c="#7CAE00" , alpha=0.3)

z = np.polyfit(Y_train,Y_lr_train_pred,1)
p = np.poly1d(z)

plt.plot(Y_train , p(Y_train) , "#F8766D")
plt.ylabel('Prediction logS')
plt.xlabel("Experimental LogS")
plt.show()