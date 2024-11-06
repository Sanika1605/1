import pandas as pd
df=pd.read_csv("uber.csv")
df.shape 
## drop unnecessary coulumns
df=df.drop(['Unnamed: 0','key','pickup_datetime'],axis=1)
df.sample(2)
df.dropna(inplace=True)
df.isnull().sum()

2.Identify Outliers
df['fare_amount'].plot.box(vert=False)

# calculate inter quartile range
q1=df['fare_amount'].quantile(0.25)
q3=df['fare_amount'].quantile(0.75)
IQR=q3-q1

lower_bound=q1-1.5*IQR
upper_bound=q3+1.5*IQR

#reomve outliers
df=df[(df['fare_amount']>=lower_bound) & (df['fare_amount']<=upper_bound)]

df['fare_amount'].plot.box(vert=False)

import matplotlib.pyplot as plt
import numpy as np
plt.subplot(3,2,1)
plt.title("Fare amount")
df['fare_amount'].plot.box(vert=False)

plt.subplot(3,2,2)
plt.title("Pickup Longitude")
df['pickup_longitude'].plot.box(vert=False)

plt.subplot(3,2,3)
plt.title("Pickup Latitude")
df['pickup_latitude'].plot.box(vert=False)

plt.subplot(3,2,4)
plt.title("Dropoff Longitude")
df['dropoff_longitude'].plot.box(vert=False)

plt.subplot(3,2,5)
plt.title("Dropoff Latitude")
df['dropoff_latitude'].plot.box(vert=False)

plt.subplot(3,2,6)
plt.title("Passenger Count")
df['passenger_count'].plot.box(vert=False)

plt.tight_layout()

3. Check the correlation
import seaborn as sns
correlation_matrix=df.corr()
sns.heatmap(correlation_matrix)
plt.show()

#Split the data
X=df[['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count']]
Y=df['fare_amount']
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
# here random_state works as a seed , everytime we run the code it divides the dataset from the same point
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
lr_m=LinearRegression()
lr_m.fit(X_train,Y_train)

rf_m=RandomForestRegressor(n_estimators=100,random_state=42)
#In the context of the RandomForestRegressor from the sklearn.ensemble module, the n_estimators parameter specifies the number of trees in the forest.
rf_m.fit(X_train,Y_train)

# predict the values
y_lr_predict=lr_m.predict(X_test)
y_rf_predict=rf_m.predict(X_test)
print(y_lr_predict)
print(y_rf_predict)

5. Evaluate
# calculate R2 and RMSE
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error
# for linear regression
r2_lr=r2_score(Y_test,y_lr_predict)
rmse_lr=np.sqrt(mean_squared_error(Y_test,y_lr_predict))

print("For Linear Regression")
print("R-square",r2_lr)
print("RMSE ",rmse_lr)

# for Random Forest Regression
r2_rf=r2_score(Y_test,y_rf_predict)
rmse_rf=np.sqrt(mean_squared_error(Y_test,y_rf_predict))

print("For Random Forest Regression")
print("R-square",r2_rf)
print("RMSE ",rmse_rf)