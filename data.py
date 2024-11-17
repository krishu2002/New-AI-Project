# Getting DATA from Github 
# Importing Pandas
import pandas as pd
# Giving addres 
df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/delaney_solubility_with_descriptors.csv")
# printing data
# print(df)           ===--->
# Dividing data
y = df['logS']
x = df.drop("logS",axis=1)
# Spliting Data
from sklearn.model_selection import train_test_split
# Setting DATA
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.2, random_state=100)
# Checking data
# print(X_train)           ===--->
# print(X_test)            ===--->