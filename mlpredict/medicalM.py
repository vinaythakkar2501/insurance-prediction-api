import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
#reading data
data = pd.read_csv('./insurance.csv')
data.head(10)

#changing categorical features into numerics
data.replace({'sex':{'male':0,'female':1}},inplace=True)
data.replace({'smoker':{'yes':0,'no':1}},inplace=True)
data.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}},inplace=True)

#separating features and target
X = data.drop(columns='charges',axis=1)
Y = data['charges']

#spliting train and test data
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=200,)

#prediction
regressor = LinearRegression()
regressor.fit(X_train,Y_train)

#building model
with open('medical_model','wb') as f:
    pickle.dump(regressor,f)