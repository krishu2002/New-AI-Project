# importing Class
from sklearn.metrics import mean_squared_error, r2_score
# improting tested data
from Module import Y_lr_test_pred,Y_lr_train_pred
from data import df,X_test,X_train,Y_test,Y_train
# Evaluation TRAIN
lr_train_mse = mean_squared_error(Y_train,Y_lr_train_pred)
lr_train_r2 = r2_score(Y_train,Y_lr_train_pred)
#Evaluation TEST
lr_test_mse = mean_squared_error(Y_test,Y_lr_test_pred)
lr_test_r2 = r2_score(Y_test,Y_lr_test_pred)

print("LR MSE (TRAIN):",lr_train_mse)
print("LR R2 (TRAIN):",lr_train_r2)
print("LR MSE (TEST):",lr_test_mse)
print("LR R3 (TEST):",lr_test_r2)