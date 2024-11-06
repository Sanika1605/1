import pandas as pd
df=pd.read_csv("emails.csv")
df.sample(5)
# split input and output data
X=df.drop(['Email No.','Prediction'],axis=1)
Y=df['Prediction']
X.shape

import seaborn as sns
sns.countplot(x=Y)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=42)
# k- nearest neighbors

from sklearn.neighbors import KNeighborsClassifier
knn_m=KNeighborsClassifier(n_neighbors=5)
# the n_neighbors parameter specifies the number of nearest neighbors to consider when making a prediction.
knn_m.fit(X_train,Y_train)

y_pred_knn=knn_m.predict(X_test)
y_pred_knn
# evaluate
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay

ConfusionMatrixDisplay.from_predictions(Y_test,y_pred_knn)

knn_accuracy = accuracy_score(Y_test, y_pred_knn)
knn_report = classification_report(Y_test, y_pred_knn)

print("Accuracy : ",knn_accuracy)
print("Report : ",knn_report)

## Support Vector Machine

from sklearn.svm import SVC
svm_model=SVC()

svm_model.fit(X_test,Y_test)

y_pred_svm=svm_model.predict(X_test)
y_pred_svm
svm_accuracy = accuracy_score(Y_test, y_pred_svm)
svm_report = classification_report(Y_test, y_pred_svm)

print("Accuracy : ",svm_accuracy)
print("Report : ",svm_report)