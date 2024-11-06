X=df[['CreditScore','Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard','IsActiveMember', 'EstimatedSalary']]
Y=df['Exited']
Y.value_counts()

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_scaled=sc.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X_scaled,Y,test_size=0.3)

from tensorflow import keras

from keras.models import Sequential
from keras.layers import Dense

classifier=Sequential()
#adding first input layer and hidden layer
classifier.add(Dense(activation='relu',units=6,kernel_initializer="uniform"))
#adding second hidden layer
classifier.add(Dense(activation='relu',units=6,kernel_initializer="uniform"))
#adding output layer
classifier.add(Dense(activation='sigmoid',units=1,kernel_initializer="uniform"))

classifier.compile(optimizer='adam',loss="binary_crossentropy",metrics=['accuracy'])

classifier.summary()

classifier.fit(X_train,Y_train,batch_size=10,epochs=40)

y_pr=classifier.predict(X_test)

y_pr

y_pr=(y_pr>0.5)
y_pr

from sklearn.metrics import accuracy_score,classification_report
print(accuracy_score(Y_test,y_pr))